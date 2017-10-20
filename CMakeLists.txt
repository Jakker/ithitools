CMAKE_MINIMUM_REQUIRED(VERSION 2.8.11)
CMAKE_POLICY(SET CMP0003 NEW)

PROJECT(ithitools C CXX)

INCLUDE_DIRECTORIES(src lib test)

SET(ITHITOOLS_LIBRARY_FILES
   lib/AddressFilter.cpp
   lib/CaptureSummary.cpp
   lib/DnsStatHash.cpp
   lib/DnsStats.cpp
   lib/ithimetrics.cpp
   lib/pcap_reader.cpp
   lib/UsefulTransaction.cpp
)

SET(ITHITOOLS_TEST_LIBRARY_FILES
   test/CaptureTest.cpp
   test/hashtest.cpp
   test/LoadTest.cpp
   test/MergeTest.cpp
   test/MetricTest.cpp
   test/SaveTest.cpp
   test/testRfc6761.cpp
)

ADD_EXECUTABLE(ithitools 
   src/ithitools.cpp
   src/getopt.c 
   $(ITHITOOLS_LIBRARY_FILES)
)

ADD_EXECUTABLE(ithitest
   src/ithitest.cpp 
   $(ITHITOOLS_LIBRARY_FILES)
   $(ITHITOOLS_TEST_LIBRARY_FILES)
)

SET(TEST_EXES ithitest)