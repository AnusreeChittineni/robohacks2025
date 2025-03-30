cmake_minimum_required(VERSION 3.10)
project(OpenCV_Custom)

# Set OpenCV version
set(OpenCV_VERSION 4.5)

# Define paths for OpenCV and OpenCV Contrib
set(OpenCV_SOURCE_DIR "${CMAKE_SOURCE_DIR}/opencv")
set(OpenCV_CONTRIB_DIR "${CMAKE_SOURCE_DIR}/opencv_contrib")

# Enable only required OpenCV modules
set(BUILD_LIST 
    core imgproc highgui videoio aruco)

# Set CMake options to build only required modules
set(BUILD_opencv_world OFF CACHE BOOL "Disable OpenCV World Module" FORCE)
set(BUILD_opencv_apps OFF CACHE BOOL "Disable OpenCV Apps" FORCE)
set(BUILD_EXAMPLES OFF CACHE BOOL "Disable OpenCV Examples" FORCE)
set(BUILD_TESTS OFF CACHE BOOL "Disable OpenCV Tests" FORCE)
set(BUILD_DOCS OFF CACHE BOOL "Disable OpenCV Docs" FORCE)
set(BUILD_opencv_python3 ON CACHE BOOL "Enable Python Bindings" FORCE)

# Include OpenCV Modules
include_directories(${OpenCV_SOURCE_DIR}/include)

# Find OpenCV with custom modules
find_package(OpenCV REQUIRED PATHS "${OpenCV_SOURCE_DIR}/build" NO_DEFAULT_PATH)

# Create executable (Replace with your script name if needed)
add_executable(my_opencv_project main.cpp)
target_link_libraries(my_opencv_project ${OpenCV_LIBS})
