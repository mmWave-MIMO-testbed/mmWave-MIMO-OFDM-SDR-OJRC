# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.26

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/local/bin/cmake

# The command to remove a file.
RM = /usr/local/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/haocheng/MIMO-OFDM-JRC-Optimal-Beam-and-Resource-Allocation

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/haocheng/MIMO-OFDM-JRC-Optimal-Beam-and-Resource-Allocation/build

# Utility rule file for mimo_ofdm_jrc_swig_swig_doc.

# Include any custom commands dependencies for this target.
include swig/CMakeFiles/mimo_ofdm_jrc_swig_swig_doc.dir/compiler_depend.make

# Include the progress variables for this target.
include swig/CMakeFiles/mimo_ofdm_jrc_swig_swig_doc.dir/progress.make

swig/CMakeFiles/mimo_ofdm_jrc_swig_swig_doc: swig/mimo_ofdm_jrc_swig_doc.i

swig/mimo_ofdm_jrc_swig_doc.i: swig/mimo_ofdm_jrc_swig_doc_swig_docs/xml/index.xml
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/haocheng/MIMO-OFDM-JRC-Optimal-Beam-and-Resource-Allocation/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Generating python docstrings for mimo_ofdm_jrc_swig_doc"
	cd /home/haocheng/MIMO-OFDM-JRC-Optimal-Beam-and-Resource-Allocation/docs/doxygen && /usr/bin/python3 -B /home/haocheng/MIMO-OFDM-JRC-Optimal-Beam-and-Resource-Allocation/docs/doxygen/swig_doc.py /home/haocheng/MIMO-OFDM-JRC-Optimal-Beam-and-Resource-Allocation/build/swig/mimo_ofdm_jrc_swig_doc_swig_docs/xml /home/haocheng/MIMO-OFDM-JRC-Optimal-Beam-and-Resource-Allocation/build/swig/mimo_ofdm_jrc_swig_doc.i

swig/mimo_ofdm_jrc_swig_doc_swig_docs/xml/index.xml: swig/_mimo_ofdm_jrc_swig_doc_tag
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/haocheng/MIMO-OFDM-JRC-Optimal-Beam-and-Resource-Allocation/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Generating doxygen xml for mimo_ofdm_jrc_swig_doc docs"
	cd /home/haocheng/MIMO-OFDM-JRC-Optimal-Beam-and-Resource-Allocation/build/swig && ./_mimo_ofdm_jrc_swig_doc_tag
	cd /home/haocheng/MIMO-OFDM-JRC-Optimal-Beam-and-Resource-Allocation/build/swig && /usr/bin/doxygen /home/haocheng/MIMO-OFDM-JRC-Optimal-Beam-and-Resource-Allocation/build/swig/mimo_ofdm_jrc_swig_doc_swig_docs/Doxyfile

mimo_ofdm_jrc_swig_swig_doc: swig/CMakeFiles/mimo_ofdm_jrc_swig_swig_doc
mimo_ofdm_jrc_swig_swig_doc: swig/mimo_ofdm_jrc_swig_doc.i
mimo_ofdm_jrc_swig_swig_doc: swig/mimo_ofdm_jrc_swig_doc_swig_docs/xml/index.xml
mimo_ofdm_jrc_swig_swig_doc: swig/CMakeFiles/mimo_ofdm_jrc_swig_swig_doc.dir/build.make
.PHONY : mimo_ofdm_jrc_swig_swig_doc

# Rule to build all files generated by this target.
swig/CMakeFiles/mimo_ofdm_jrc_swig_swig_doc.dir/build: mimo_ofdm_jrc_swig_swig_doc
.PHONY : swig/CMakeFiles/mimo_ofdm_jrc_swig_swig_doc.dir/build

swig/CMakeFiles/mimo_ofdm_jrc_swig_swig_doc.dir/clean:
	cd /home/haocheng/MIMO-OFDM-JRC-Optimal-Beam-and-Resource-Allocation/build/swig && $(CMAKE_COMMAND) -P CMakeFiles/mimo_ofdm_jrc_swig_swig_doc.dir/cmake_clean.cmake
.PHONY : swig/CMakeFiles/mimo_ofdm_jrc_swig_swig_doc.dir/clean

swig/CMakeFiles/mimo_ofdm_jrc_swig_swig_doc.dir/depend:
	cd /home/haocheng/MIMO-OFDM-JRC-Optimal-Beam-and-Resource-Allocation/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/haocheng/MIMO-OFDM-JRC-Optimal-Beam-and-Resource-Allocation /home/haocheng/MIMO-OFDM-JRC-Optimal-Beam-and-Resource-Allocation/swig /home/haocheng/MIMO-OFDM-JRC-Optimal-Beam-and-Resource-Allocation/build /home/haocheng/MIMO-OFDM-JRC-Optimal-Beam-and-Resource-Allocation/build/swig /home/haocheng/MIMO-OFDM-JRC-Optimal-Beam-and-Resource-Allocation/build/swig/CMakeFiles/mimo_ofdm_jrc_swig_swig_doc.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : swig/CMakeFiles/mimo_ofdm_jrc_swig_swig_doc.dir/depend
