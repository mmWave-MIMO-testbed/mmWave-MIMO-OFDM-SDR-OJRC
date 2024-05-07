import time
import os
import sys
import host
import multiprocessing
import connect
from common import *



def get_args():
    import argparse
    parser = argparse.ArgumentParser(description='Command line options.')
    parser.add_argument('-s', '--serial', dest='serial_num', metavar='Serial number', default=None,
                         help='Specify MB serial name')
    parser.add_argument('-b', '--bsp', dest='bsp', choices=['rapvalbsp','rapvalx','rapvalt','bfm02803','dbm1','none'], default='rapvalbsp',
                         help='Specify type of BSP')
    parser.add_argument('-n', '--no_diff', dest='ref_is_diff', action='store_false',
                         help='Set this flag if reference clock is NOT differential')
    parser.add_argument('-i', '--spi', dest='fspi', metavar='<spi_freq>', default=None,
                         help='Specify SPI clock frequency <spi_freq>')
    parser.add_argument('-r', '--fref', dest='fref', metavar='<ref_freq>', default=None,
                         help='Specify reference clock frequency <ref_freq>')
    parser.add_argument('-d', '--fdig', dest='fdig', metavar='<dig_freq>', default=None,
                         help='Specify digital clock frequency <dig_freq>')
    parser.add_argument('-f', '--flo', dest='flo', metavar='<lo_freq>', default=None,
                         help='Specify LO clock frequency <lo_freq>')
    parser.add_argument('-t', '--test', dest='test', default=None,
                         help='Specify test')
    parser.add_argument('-c', '--cfg', dest='cfg_file', metavar='<cfg filename>', default=None,
                         help='Specify configuration file name')
    parser.add_argument('-g', '--gui', dest='gui', metavar='rap? | rap? rap? ... | rapAll', nargs='*', default=None,
                         help='Start GUI[s]')
    parser.add_argument('-x', '--xgui', dest='xgui', metavar='rap? | rap? rap? ... | rapAll', nargs='*', default=None,
                         help='Start GUI[s] with extended features')
    return parser.parse_args()
    
def info_file(fname="evk.info"):
    import evk_logger
    evk_logger.evk_logger = evk_logger.EvkLogger(fname)
    return evk_logger.evk_logger

# class Connect_instance:
    
#     def __init__(self, serial_num, bsp, clock_rate=10000000):
#         print("111")
#         import mbdrv  # Importing mbdrv module here
#         print("222")
#         self.serial_num = serial_num
#         print("333")
#         self.mb         = mbdrv.MbDrv()
#         print("444")
#         self.board_id  = self.mb.get_board_id(serial_num)
#         print("555")

class Connect_instance:
    def __init__(self, serial_num, bsp, clock_rate=10000000):
        # import mbdrv
        self.serial_num = serial_num
        print("333")
        self.mb         = mbdrv.MbDrv()
        print("444")
        self.board_id  = self.mb.get_board_id(serial_num)

def connect_to_device(serial_num, args, info_logger, mb, fref=None, fdig=None, flo=None, fspi=None):
    if serial_num != '':
        board_id   = mb.get_board_id(serial_num)
        board_type = mb.get_board_type(board_id)
        info_logger.log_info('Connecting to motherboard {0} with serial number {1} ...'.format(board_type, serial_num),2)
        Connect_instance(serial_num, 'rapvalt', 1000000)
        host_instance = host.Host(serial_num=serial_num, bsp=args.bsp, fref=fref, fdig=fdig, flo=flo, fspi=fspi, indent=2)
        rapAll = []
        for num in range(0,host.chip._chip_info.get_num_devs()):
            exec("rap{:} = host.rap{:}".format(num,num))
            exec("rapAll.append(rap{:})".format(str(num)))

        if args.gui != None:
            if len(args.gui) == 0:
                guis = rapAll
            else:
                guis = []
                for gui in args.gui:
                    guis.append(eval(gui))
            host.open_gui(guis)

        if args.xgui != None:
            if len(args.xgui) == 0:
                guis = rapAll
            else:
                guis = []
                for gui in args.xgui:
                    guis.append(eval(gui))
            host.open_gui(guis, extended=True)


        if args.test != None:
            if not args.test.endswith('.py'):
                args.test = args.test+'.py'
            if os.path.isfile(args.test):
                test_file_exist = True
            else:
                test_file_exist = False
                for dir in ['tests']:
                    if os.path.isfile(os.path.join(dir,args.test)):
                        args.test = os.path.join(dir,args.test)
                        test_file_exist = True
                        break
                if not test_file_exist:
                    info_logger.log_error('No file found matching {}'.format(args.test),2)
                    possible_test_files = []
                    for dir in ['tests']+sys.path:
                        if os.path.isfile(os.path.join(dir,os.path.basename(args.test))):
                            possible_test_files.append(os.path.join(dir,os.path.basename(args.test)))
                    if len(possible_test_files) > 0:
                        info_logger.log_error('Maybe you meant one of these files?',4)
                        for file in possible_test_files:
                            info_logger.log_error(file,4)
            if test_file_exist:
                info_logger.log_info('Running file {}'.format(args.test),2)
                t=open(args.test,'r')
                exec(t.read())
                t.close()
    info_logger.delayed_reset()


if __name__ == "__main__":
    if sys.platform == 'linux':
        print('  Unloading USB Serial driver...')
        os.system('sudo modprobe -r ftdi_sio')
    args = get_args()
    #cmd_hist_file()
    info_logger=info_file()
    import rlcompleter, readline
    readline.set_history_length(1000)
    readline.parse_and_bind('tab:complete')
    import fileHandler as json
    #info_logger=info_file()
    try:
        fref = float(args.fref)
    except:
        fref = None

    try:
        fdig = float(args.fdig)
    except:
        fdig = None
        
    try:
        flo = float(args.flo)
    except:
        flo = None
        
    try:
        fspi = int(args.fspi)
    except:
        fspi = None

    
    try:
        info_logger.log_info('Trying to import module MB',2)
        import mbdrv
        mb = mbdrv.MbDrv()
    except ImportError as ie:
        info_logger.log_error("Error! " + str(ie),2)
        sys.exit()

    info_logger.log_info('MB {:} import successful.'.format(mb.version()),2+2)
    if args.serial_num == None:
        info_logger.log_info('Available motherboards:',2)
        nof_channels = int(mb.num_of_channels())
        if nof_channels > 0:
            mbs = {}
            for chan in range(0,nof_channels):
                mb_num = mb.get_channel_info(chan)['SerialNumber'][:-1]
                if mb_num != '':
                    mbs[mb_num] = mb.get_channel_info(chan)
            for mb_num in mbs:
                info_logger.log_info('{}'.format(mb_num),2+2)
            info_logger.log_info('')
            if all(key in mbs.keys() for key in ["T582306548", "T582306549"]):
                serial_num1 = "T582306548"
                serial_num2 = "T582306549"
        else:
            info_logger.log_info('No motherboard detected. Exiting ...')
            sys.exit()
    else:
        serial_num1 = args.serial_num

    process1 = multiprocessing.Process(target=connect_to_device,
                                                    args=(serial_num1, args, info_logger, mb, fref, fdig, flo, fspi))
    process2 = multiprocessing.Process(target=connect_to_device,
                                                    args=(serial_num2, args, info_logger, mb, fref, fdig, flo, fspi))

    process1.start()
    # process2.start()

    process1.join()
    # process2.join()