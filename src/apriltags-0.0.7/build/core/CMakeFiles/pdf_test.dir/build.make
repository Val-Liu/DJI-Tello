# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.5

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/valliu/桌面/apriltags-0.0.7

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/valliu/桌面/apriltags-0.0.7/build

# Include any dependencies generated for this target.
include core/CMakeFiles/pdf_test.dir/depend.make

# Include the progress variables for this target.
include core/CMakeFiles/pdf_test.dir/progress.make

# Include the compile flags for this target's objects.
include core/CMakeFiles/pdf_test.dir/flags.make

core/CMakeFiles/pdf_test.dir/contrib/pdf_test.cpp.o: core/CMakeFiles/pdf_test.dir/flags.make
core/CMakeFiles/pdf_test.dir/contrib/pdf_test.cpp.o: ../core/contrib/pdf_test.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/valliu/桌面/apriltags-0.0.7/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object core/CMakeFiles/pdf_test.dir/contrib/pdf_test.cpp.o"
	cd /home/valliu/桌面/apriltags-0.0.7/build/core && /usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/pdf_test.dir/contrib/pdf_test.cpp.o -c /home/valliu/桌面/apriltags-0.0.7/core/contrib/pdf_test.cpp

core/CMakeFiles/pdf_test.dir/contrib/pdf_test.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/pdf_test.dir/contrib/pdf_test.cpp.i"
	cd /home/valliu/桌面/apriltags-0.0.7/build/core && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/valliu/桌面/apriltags-0.0.7/core/contrib/pdf_test.cpp > CMakeFiles/pdf_test.dir/contrib/pdf_test.cpp.i

core/CMakeFiles/pdf_test.dir/contrib/pdf_test.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/pdf_test.dir/contrib/pdf_test.cpp.s"
	cd /home/valliu/桌面/apriltags-0.0.7/build/core && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/valliu/桌面/apriltags-0.0.7/core/contrib/pdf_test.cpp -o CMakeFiles/pdf_test.dir/contrib/pdf_test.cpp.s

core/CMakeFiles/pdf_test.dir/contrib/pdf_test.cpp.o.requires:

.PHONY : core/CMakeFiles/pdf_test.dir/contrib/pdf_test.cpp.o.requires

core/CMakeFiles/pdf_test.dir/contrib/pdf_test.cpp.o.provides: core/CMakeFiles/pdf_test.dir/contrib/pdf_test.cpp.o.requires
	$(MAKE) -f core/CMakeFiles/pdf_test.dir/build.make core/CMakeFiles/pdf_test.dir/contrib/pdf_test.cpp.o.provides.build
.PHONY : core/CMakeFiles/pdf_test.dir/contrib/pdf_test.cpp.o.provides

core/CMakeFiles/pdf_test.dir/contrib/pdf_test.cpp.o.provides.build: core/CMakeFiles/pdf_test.dir/contrib/pdf_test.cpp.o


# Object files for target pdf_test
pdf_test_OBJECTS = \
"CMakeFiles/pdf_test.dir/contrib/pdf_test.cpp.o"

# External object files for target pdf_test
pdf_test_EXTERNAL_OBJECTS =

pdf_test: core/CMakeFiles/pdf_test.dir/contrib/pdf_test.cpp.o
pdf_test: core/CMakeFiles/pdf_test.dir/build.make
pdf_test: lib/libapriltag.so
pdf_test: core/CMakeFiles/pdf_test.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/valliu/桌面/apriltags-0.0.7/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable ../pdf_test"
	cd /home/valliu/桌面/apriltags-0.0.7/build/core && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/pdf_test.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
core/CMakeFiles/pdf_test.dir/build: pdf_test

.PHONY : core/CMakeFiles/pdf_test.dir/build

core/CMakeFiles/pdf_test.dir/requires: core/CMakeFiles/pdf_test.dir/contrib/pdf_test.cpp.o.requires

.PHONY : core/CMakeFiles/pdf_test.dir/requires

core/CMakeFiles/pdf_test.dir/clean:
	cd /home/valliu/桌面/apriltags-0.0.7/build/core && $(CMAKE_COMMAND) -P CMakeFiles/pdf_test.dir/cmake_clean.cmake
.PHONY : core/CMakeFiles/pdf_test.dir/clean

core/CMakeFiles/pdf_test.dir/depend:
	cd /home/valliu/桌面/apriltags-0.0.7/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/valliu/桌面/apriltags-0.0.7 /home/valliu/桌面/apriltags-0.0.7/core /home/valliu/桌面/apriltags-0.0.7/build /home/valliu/桌面/apriltags-0.0.7/build/core /home/valliu/桌面/apriltags-0.0.7/build/core/CMakeFiles/pdf_test.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : core/CMakeFiles/pdf_test.dir/depend

