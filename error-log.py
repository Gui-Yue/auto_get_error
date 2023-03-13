aptitude
[ 1776s] make[6]: Nothing to be done for 'all'.
[ 1776s] make[6]: Leaving directory '/usr/src/packages/BUILD/build/src/generic/util/mocks'
[ 1776s] make[6]: Entering directory '/usr/src/packages/BUILD/build/src/generic/util'
[ 1776s] g++ -DLOCALEDIR=\"/usr/share/locale\" -DHAVE_CONFIG_H -I. -I../../../../src/generic/util -I../../..  -I../../.. -I../../../../src/generic/util -I../../../.. -I../../../../src -I/usr/include -Wdate-time -D_FORTIFY_SOURCE=2 -DHELPDIR=\"/usr/share/aptitude\" -DPKGDATADIR=\"/usr/share/aptitude\"  -I/usr/include/sigc++-2.0 -I/usr/lib/riscv64-linux-gnu/sigc++-2.0/include -I/usr/include/cwidget -I/usr/lib/riscv64-linux-gnu/cwidget -I/usr/include/sigc++-2.0 -I/usr/lib/riscv64-linux-gnu/sigc++-2.0/include    -g -O2 -ffile-prefix-map=/usr/src/packages/BUILD=. -fstack-protector-strong -Wformat -Werror=format-security  -D_REENTRANT -std=gnu++17 -Wall  -c -o file_cache.o ../../../../src/generic/util/file_cache.cc
[ 1776s] g++ -DLOCALEDIR=\"/usr/share/locale\" -DHAVE_CONFIG_H -I. -I../../../../src/generic/util -I../../..  -I../../.. -I../../../../src/generic/util -I../../../.. -I../../../../src -I/usr/include -Wdate-time -D_FORTIFY_SOURCE=2 -DHELPDIR=\"/usr/share/aptitude\" -DPKGDATADIR=\"/usr/share/aptitude\"  -I/usr/include/sigc++-2.0 -I/usr/lib/riscv64-linux-gnu/sigc++-2.0/include -I/usr/include/cwidget -I/usr/lib/riscv64-linux-gnu/cwidget -I/usr/include/sigc++-2.0 -I/usr/lib/riscv64-linux-gnu/sigc++-2.0/include    -g -O2 -ffile-prefix-map=/usr/src/packages/BUILD=. -fstack-protector-strong -Wformat -Werror=format-security  -D_REENTRANT -std=gnu++17 -Wall  -c -o logging.o ../../../../src/generic/util/logging.cc
[ 1821s] g++ -DLOCALEDIR=\"/usr/share/locale\" -DHAVE_CONFIG_H -I. -I../../../../src/generic/util -I../../..  -I../../.. -I../../../../src/generic/util -I../../../.. -I../../../../src -I/usr/include -Wdate-time -D_FORTIFY_SOURCE=2 -DHELPDIR=\"/usr/share/aptitude\" -DPKGDATADIR=\"/usr/share/aptitude\"  -I/usr/include/sigc++-2.0 -I/usr/lib/riscv64-linux-gnu/sigc++-2.0/include -I/usr/include/cwidget -I/usr/lib/riscv64-linux-gnu/cwidget -I/usr/include/sigc++-2.0 -I/usr/lib/riscv64-linux-gnu/sigc++-2.0/include    -g -O2 -ffile-prefix-map=/usr/src/packages/BUILD=. -fstack-protector-strong -Wformat -Werror=format-security  -D_REENTRANT -std=gnu++17 -Wall  -c -o progress_info.o ../../../../src/generic/util/progress_info.cc
[ 1833s] g++ -DLOCALEDIR=\"/usr/share/locale\" -DHAVE_CONFIG_H -I. -I../../../../src/generic/util -I../../..  -I../../.. -I../../../../src/generic/util -I../../../.. -I../../../../src -I/usr/include -Wdate-time -D_FORTIFY_SOURCE=2 -DHELPDIR=\"/usr/share/aptitude\" -DPKGDATADIR=\"/usr/share/aptitude\"  -I/usr/include/sigc++-2.0 -I/usr/lib/riscv64-linux-gnu/sigc++-2.0/include -I/usr/include/cwidget -I/usr/lib/riscv64-linux-gnu/cwidget -I/usr/include/sigc++-2.0 -I/usr/lib/riscv64-linux-gnu/sigc++-2.0/include    -g -O2 -ffile-prefix-map=/usr/src/packages/BUILD=. -fstack-protector-strong -Wformat -Werror=format-security  -D_REENTRANT -std=gnu++17 -Wall  -c -o refcounted_base.o ../../../../src/generic/util/refcounted_base.cc
[ 1838s] In file included from ../../../../src/generic/util/refcounted_base.h:25,
[ 1838s]                  from ../../../../src/generic/util/refcounted_base.cc:20:
[ 1838s] /usr/include/cwidget/generic/threads/threads.h: In constructor 'cwidget::threads::thread::attr::attr()':
[ 1838s] /usr/include/cwidget/generic/threads/threads.h:139:11: error: 'pthread_attr_init' was not declared in this scope; did you mean 'pthread_attr_t'?
[ 1838s]   139 |           pthread_attr_init(&attrs);
[ 1838s]       |           ^~~~~~~~~~~~~~~~~
[ 1838s]       |           pthread_attr_t
[ 1838s] /usr/include/cwidget/generic/threads/threads.h: In destructor 'cwidget::threads::thread::attr::~attr()':
[ 1838s] /usr/include/cwidget/generic/threads/threads.h:144:11: error: 'pthread_attr_destroy' was not declared in this scope; did you mean 'pthread_attr_t'?


kidentitymanagement
[ 1585s] [ 43%] Building CXX object src/CMakeFiles/KF5IdentityManagement.dir/identitymanager.cpp.o
[ 1585s] cd /usr/src/packages/BUILD/obj-riscv64-linux-gnu/src && /usr/bin/c++ -DKCOREADDONS_LIB -DKF5IdentityManagement_EXPORTS -DKF_DEPRECATED_WARNINGS_SINCE=0x060000 -DKF_DISABLE_DEPRECATED_BEFORE_AND_AT=0x055000 -DQT_CONCURRENT_LIB -DQT_CORE_LIB -DQT_DBUS_LIB -DQT_DEPRECATED_WARNINGS_SINCE=0x060000 -DQT_DISABLE_DEPRECATED_BEFORE=0x050f00 -DQT_GUI_LIB -DQT_NETWORK_LIB -DQT_NO_CAST_FROM_ASCII -DQT_NO_CAST_FROM_BYTEARRAY -DQT_NO_CAST_TO_ASCII -DQT_NO_DEBUG -DQT_NO_FOREACH -DQT_NO_KEYWORDS -DQT_NO_NARROWING_CONVERSIONS_IN_CONNECT -DQT_NO_URL_CAST_FROM_STRING -DQT_STRICT_ITERATORS -DQT_USE_QSTRINGBUILDER -DQT_WIDGETS_LIB -DQT_XML_LIB -DTRANSLATION_DOMAIN=\"libkpimidentities5\" -D_GNU_SOURCE -D_LARGEFILE64_SOURCE -I/usr/src/packages/BUILD/obj-riscv64-linux-gnu/src -I/usr/src/packages/BUILD/src -I/usr/src/packages/BUILD/obj-riscv64-linux-gnu/src/KF5IdentityManagement_autogen/include -isystem /usr/include/KF5/KCoreAddons -isystem /usr/include/KF5 -isystem /usr/include/riscv64-linux-gnu/qt5 -isystem /usr/include/riscv64-linux-gnu/qt5/QtCore -isystem /usr/lib/riscv64-linux-gnu/qt5/mkspecs/linux-g++ -isystem /usr/include/KF5/KPIMTextEdit -isystem /usr/include/KF5/KCodecs -isystem /usr/include/riscv64-linux-gnu/qt5/QtNetwork -isystem /usr/include/KF5/KI18n -isystem /usr/include/KF5/KWidgetsAddons -isystem /usr/include/riscv64-linux-gnu/qt5/QtWidgets -isystem /usr/include/riscv64-linux-gnu/qt5/QtGui -isystem /usr/include/KF5/KXmlGui -isystem /usr/include/riscv64-linux-gnu/qt5/QtXml -isystem /usr/include/KF5/KConfigCore -isystem /usr/include/KF5/KConfigWidgets -isystem /usr/include/KF5/KConfigGui -isystem /usr/include/KF5/KAuth -isystem /usr/include/riscv64-linux-gnu/qt5/QtDBus -isystem /usr/include/KF5/KIOWidgets -isystem /usr/include/KF5/KIOGui -isystem /usr/include/KF5/KIOCore -isystem /usr/include/KF5/KService -isystem /usr/include/riscv64-linux-gnu/qt5/QtConcurrent -isystem /usr/include/KF5/KWindowSystem -isystem /usr/include/KF5/KJobWidgets -isystem /usr/include/KF5/Solid -isystem /usr/include/KF5/KCompletion -g -O2 -ffile-prefix-map=/usr/src/packages/BUILD=. -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -fno-operator-names -fno-exceptions -Wall -Wextra -Wcast-align -Wchar-subscripts -Wformat-security -Wno-long-long -Wpointer-arith -Wundef -Wnon-virtual-dtor -Woverloaded-virtual -Werror=return-type -Werror=init-self -Wvla -Wdate-time -Wsuggest-override -Wlogical-op -pedantic -Wzero-as-null-pointer-constant -fPIC -fvisibility=hidden -fvisibility-inlines-hidden -fPIC -std=gnu++17 -MD -MT src/CMakeFiles/KF5IdentityManagement.dir/identitymanager.cpp.o -MF CMakeFiles/KF5IdentityManagement.dir/identitymanager.cpp.o.d -o CMakeFiles/KF5IdentityManagement.dir/identitymanager.cpp.o -c /usr/src/packages/BUILD/src/identitymanager.cpp
[ 1587s] [ 47%] Building CXX object src/CMakeFiles/KF5IdentityManagement.dir/signature.cpp.o
[ 1587s] cd /usr/src/packages/BUILD/obj-riscv64-linux-gnu/src && /usr/bin/c++ -DKCOREADDONS_LIB -DKF5IdentityManagement_EXPORTS -DKF_DEPRECATED_WARNINGS_SINCE=0x060000 -DKF_DISABLE_DEPRECATED_BEFORE_AND_AT=0x055000 -DQT_CONCURRENT_LIB -DQT_CORE_LIB -DQT_DBUS_LIB -DQT_DEPRECATED_WARNINGS_SINCE=0x060000 -DQT_DISABLE_DEPRECATED_BEFORE=0x050f00 -DQT_GUI_LIB -DQT_NETWORK_LIB -DQT_NO_CAST_FROM_ASCII -DQT_NO_CAST_FROM_BYTEARRAY -DQT_NO_CAST_TO_ASCII -DQT_NO_DEBUG -DQT_NO_FOREACH -DQT_NO_KEYWORDS -DQT_NO_NARROWING_CONVERSIONS_IN_CONNECT -DQT_NO_URL_CAST_FROM_STRING -DQT_STRICT_ITERATORS -DQT_USE_QSTRINGBUILDER -DQT_WIDGETS_LIB -DQT_XML_LIB -DTRANSLATION_DOMAIN=\"libkpimidentities5\" -D_GNU_SOURCE -D_LARGEFILE64_SOURCE -I/usr/src/packages/BUILD/obj-riscv64-linux-gnu/src -I/usr/src/packages/BUILD/src -I/usr/src/packages/BUILD/obj-riscv64-linux-gnu/src/KF5IdentityManagement_autogen/include -isystem /usr/include/KF5/KCoreAddons -isystem /usr/include/KF5 -isystem /usr/include/riscv64-linux-gnu/qt5 -isystem /usr/include/riscv64-linux-gnu/qt5/QtCore -isystem /usr/lib/riscv64-linux-gnu/qt5/mkspecs/linux-g++ -isystem /usr/include/KF5/KPIMTextEdit -isystem /usr/include/KF5/KCodecs -isystem /usr/include/riscv64-linux-gnu/qt5/QtNetwork -isystem /usr/include/KF5/KI18n -isystem /usr/include/KF5/KWidgetsAddons -isystem /usr/include/riscv64-linux-gnu/qt5/QtWidgets -isystem /usr/include/riscv64-linux-gnu/qt5/QtGui -isystem /usr/include/KF5/KXmlGui -isystem /usr/include/riscv64-linux-gnu/qt5/QtXml -isystem /usr/include/KF5/KConfigCore -isystem /usr/include/KF5/KConfigWidgets -isystem /usr/include/KF5/KConfigGui -isystem /usr/include/KF5/KAuth -isystem /usr/include/riscv64-linux-gnu/qt5/QtDBus -isystem /usr/include/KF5/KIOWidgets -isystem /usr/include/KF5/KIOGui -isystem /usr/include/KF5/KIOCore -isystem /usr/include/KF5/KService -isystem /usr/include/riscv64-linux-gnu/qt5/QtConcurrent -isystem /usr/include/KF5/KWindowSystem -isystem /usr/include/KF5/KJobWidgets -isystem /usr/include/KF5/Solid -isystem /usr/include/KF5/KCompletion -g -O2 -ffile-prefix-map=/usr/src/packages/BUILD=. -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -fno-operator-names -fno-exceptions -Wall -Wextra -Wcast-align -Wchar-subscripts -Wformat-security -Wno-long-long -Wpointer-arith -Wundef -Wnon-virtual-dtor -Woverloaded-virtual -Werror=return-type -Werror=init-self -Wvla -Wdate-time -Wsuggest-override -Wlogical-op -pedantic -Wzero-as-null-pointer-constant -fPIC -fvisibility=hidden -fvisibility-inlines-hidden -fPIC -std=gnu++17 -MD -MT src/CMakeFiles/KF5IdentityManagement.dir/signature.cpp.o -MF CMakeFiles/KF5IdentityManagement.dir/signature.cpp.o.d -o CMakeFiles/KF5IdentityManagement.dir/signature.cpp.o -c /usr/src/packages/BUILD/src/signature.cpp
[ 1614s] In file included from /usr/include/riscv64-linux-gnu/qt5/QtCore/qglobal.h:105,
[ 1614s]                  from /usr/include/riscv64-linux-gnu/qt5/QtCore/qchar.h:43,
[ 1614s]                  from /usr/include/riscv64-linux-gnu/qt5/QtCore/qhash.h:44,
[ 1614s]                  from /usr/include/riscv64-linux-gnu/qt5/QtCore/QHash:1,
[ 1614s]                  from /usr/src/packages/BUILD/src/signature.h:14,
[ 1614s]                  from /usr/src/packages/BUILD/src/signature.cpp:9:
[ 1614s] /usr/include/KF5/KPIMTextEdit/kpimtextedit/richtextcomposerimages.h:99:12: error: standard attributes in middle of decl-specifiers
[ 1614s]    99 |     static Q_REQUIRED_RESULT QByteArray imageNamesToContentIds(const QByteArray &htmlBody, const ImageList &imageList);
[ 1614s]       |            ^~~~~~~~~~~~~~~~~
[ 1614s] /usr/include/KF5/KPIMTextEdit/kpimtextedit/richtextcomposerimages.h:99:12: note: standard attributes must precede the decl-specifiers to apply to the declaration, or follow them to apply to the type
[ 1619s] make[3]: *** [src/CMakeFiles/KF5IdentityManagement.dir/build.make:161: src/CMakeFiles/KF5IdentityManagement.dir/signature.cpp.o] Error 1
[ 1619s] make[3]: *** Waiting for unfinished jobs....


libxcb
[  624s] configure:5153: checking for unistd.h
[  624s] configure:5153: gcc -c -g -O2 -ffile-prefix-map=/usr/src/packages/BUILD=. -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 conftest.c >&5
[  624s] configure:5153: $? = 0
[  624s] configure:5153: result: yes
[  624s] configure:5153: checking for wchar.h
[  624s] configure:5153: gcc -c -g -O2 -ffile-prefix-map=/usr/src/packages/BUILD=. -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 conftest.c >&5
[  624s] configure:5153: $? = 0
[  624s] configure:5153: result: yes
[  624s] configure:5153: checking for minix/config.h
[  624s] configure:5153: gcc -c -g -O2 -ffile-prefix-map=/usr/src/packages/BUILD=. -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 conftest.c >&5
[  624s] conftest.c:49:10: fatal error: minix/config.h: No such file or directory
[  624s]    49 | #include <minix/config.h>
[  624s]       |          ^~~~~~~~~~~~~~~~
[  624s] compilation terminated.
[  624s] configure:5153: $? = 1
[  624s] configure: failed program was:


nas
[  643s] make[3]: Entering directory '/usr/src/packages/BUILD/server'
[  643s] making all in server/dia...
[  643s] make[4]: Entering directory '/usr/src/packages/BUILD/server/dia'
[  643s] rm -f dispatch.o
[  643s] gcc -c -O -g -O2 -ffile-prefix-map=/usr/src/packages/BUILD=. -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -fcommon   -I. -I../include -I../../include -I../../lib/audio -I../../include    -Dlinux LinuxMachineDefines -D_POSIX_C_SOURCE=199309L 				-D_POSIX_SOURCE -D_XOPEN_SOURCE 				-D_BSD_SOURCE -D_SVID_SOURCE                                 -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 				  				  -DFUNCPROTO=15 -DNARROWPROTO   -DNASCONFSEARCHPATH=\"/etc/nas/\"   dispatch.c
[  644s] In file included from /usr/include/riscv64-linux-gnu/bits/libc-header-start.h:33,
[  644s]                  from /usr/include/string.h:26,
[  644s]                  from ../include/os.h:124,
[  644s]                  from ../include/misc.h:57,
[  644s]                  from dispatch.c:52:
[  644s] /usr/include/features.h:194:3: warning: #warning "_BSD_SOURCE and _SVID_SOURCE are deprecated, use _DEFAULT_SOURCE" [-Wcpp]
[  644s]   194 | # warning "_BSD_SOURCE and _SVID_SOURCE are deprecated, use _DEFAULT_SOURCE"
[  644s]       |   ^~~~~~~
[  646s] gcc: warning: LinuxMachineDefines: linker input file unused because linking not done
[  646s] gcc: error: LinuxMachineDefines: linker input file not found: No such file or directory
[  646s] make[4]: *** [Makefile:1077: dispatch.o] Error 1


opencolorio
[ 1955s] cd /usr/src/packages/BUILD/debian/cmake/src/core && /usr/bin/c++ -DOpenColorIO_EXPORTS -I/usr/src/packages/BUILD/export -I/usr/src/packages/BUILD/debian/cmake/export -I/usr/src/packages/BUILD/ext/oiio/src/include -I/usr/src/packages/BUILD/debian/cmake/ext/dist/include -g -O2 -ffile-prefix-map=/usr/src/packages/BUILD=. -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -Wall -Wextra -Wshadow -Wconversion -Wcast-qual -Wformat=2 -fPIC -DTIXML_USE_STL   -fPIC -fvisibility=hidden -Werror -MD -MT src/core/CMakeFiles/OpenColorIO.dir/AllocationTransform.cpp.o -MF CMakeFiles/OpenColorIO.dir/AllocationTransform.cpp.o.d -o CMakeFiles/OpenColorIO.dir/AllocationTransform.cpp.o -c /usr/src/packages/BUILD/src/core/AllocationTransform.cpp
[ 1955s] [  1%] Building CXX object src/core/CMakeFiles/OpenColorIO.dir/AllocationOp.cpp.o
[ 1955s] cd /usr/src/packages/BUILD/debian/cmake/src/core && /usr/bin/c++ -DOpenColorIO_EXPORTS -I/usr/src/packages/BUILD/export -I/usr/src/packages/BUILD/debian/cmake/export -I/usr/src/packages/BUILD/ext/oiio/src/include -I/usr/src/packages/BUILD/debian/cmake/ext/dist/include -g -O2 -ffile-prefix-map=/usr/src/packages/BUILD=. -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -Wall -Wextra -Wshadow -Wconversion -Wcast-qual -Wformat=2 -fPIC -DTIXML_USE_STL   -fPIC -fvisibility=hidden -Werror -MD -MT src/core/CMakeFiles/OpenColorIO.dir/AllocationOp.cpp.o -MF CMakeFiles/OpenColorIO.dir/AllocationOp.cpp.o.d -o CMakeFiles/OpenColorIO.dir/AllocationOp.cpp.o -c /usr/src/packages/BUILD/src/core/AllocationOp.cpp
[ 1965s] [  2%] Building CXX object src/core/CMakeFiles/OpenColorIO.dir/Baker.cpp.o
[ 1965s] cd /usr/src/packages/BUILD/debian/cmake/src/core && /usr/bin/c++ -DOpenColorIO_EXPORTS -I/usr/src/packages/BUILD/export -I/usr/src/packages/BUILD/debian/cmake/export -I/usr/src/packages/BUILD/ext/oiio/src/include -I/usr/src/packages/BUILD/debian/cmake/ext/dist/include -g -O2 -ffile-prefix-map=/usr/src/packages/BUILD=. -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -Wall -Wextra -Wshadow -Wconversion -Wcast-qual -Wformat=2 -fPIC -DTIXML_USE_STL   -fPIC -fvisibility=hidden -Werror -MD -MT src/core/CMakeFiles/OpenColorIO.dir/Baker.cpp.o -MF CMakeFiles/OpenColorIO.dir/Baker.cpp.o.d -o CMakeFiles/OpenColorIO.dir/Baker.cpp.o -c /usr/src/packages/BUILD/src/core/Baker.cpp
[ 1966s] [  3%] Building CXX object src/core/CMakeFiles/OpenColorIO.dir/CDLTransform.cpp.o
[ 1966s] cd /usr/src/packages/BUILD/debian/cmake/src/core && /usr/bin/c++ -DOpenColorIO_EXPORTS -I/usr/src/packages/BUILD/export -I/usr/src/packages/BUILD/debian/cmake/export -I/usr/src/packages/BUILD/ext/oiio/src/include -I/usr/src/packages/BUILD/debian/cmake/ext/dist/include -g -O2 -ffile-prefix-map=/usr/src/packages/BUILD=. -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -Wall -Wextra -Wshadow -Wconversion -Wcast-qual -Wformat=2 -fPIC -DTIXML_USE_STL   -fPIC -fvisibility=hidden -Werror -MD -MT src/core/CMakeFiles/OpenColorIO.dir/CDLTransform.cpp.o -MF CMakeFiles/OpenColorIO.dir/CDLTransform.cpp.o.d -o CMakeFiles/OpenColorIO.dir/CDLTransform.cpp.o -c /usr/src/packages/BUILD/src/core/CDLTransform.cpp
[ 1978s] [  4%] Building CXX object src/core/CMakeFiles/OpenColorIO.dir/Caching.cpp.o
[ 1978s] cd /usr/src/packages/BUILD/debian/cmake/src/core && /usr/bin/c++ -DOpenColorIO_EXPORTS -I/usr/src/packages/BUILD/export -I/usr/src/packages/BUILD/debian/cmake/export -I/usr/src/packages/BUILD/ext/oiio/src/include -I/usr/src/packages/BUILD/debian/cmake/ext/dist/include -g -O2 -ffile-prefix-map=/usr/src/packages/BUILD=. -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -Wall -Wextra -Wshadow -Wconversion -Wcast-qual -Wformat=2 -fPIC -DTIXML_USE_STL   -fPIC -fvisibility=hidden -Werror -MD -MT src/core/CMakeFiles/OpenColorIO.dir/Caching.cpp.o -MF CMakeFiles/OpenColorIO.dir/Caching.cpp.o.d -o CMakeFiles/OpenColorIO.dir/Caching.cpp.o -c /usr/src/packages/BUILD/src/core/Caching.cpp
[ 1986s] In file included from /usr/src/packages/BUILD/src/core/Caching.cpp:32:
[ 1986s] /usr/src/packages/BUILD/src/core/PathUtils.h:58:29: error: 'template<class _Arg1, class _Arg2, class _Result> struct std::binary_function' is deprecated [-Werror=deprecated-declarations]
[ 1986s]    58 |     struct EnvMapKey : std::binary_function <T, T, bool>
[ 1986s]       |                             ^~~~~~~~~~~~~~~
[ 1986s] In file included from /usr/include/c++/12/string:48,
[ 1986s]                  from /usr/src/packages/BUILD/export/OpenColorIO/OpenColorIO.h:35,
[ 1986s]                  from /usr/src/packages/BUILD/src/core/Caching.cpp:29:


petsc
[ 2155s] # 0 "<built-in>"
[ 2155s] # 0 "<command-line>"
[ 2155s] # 1 "/usr/include/stdc-predef.h" 1 3 4
[ 2155s] # 0 "<command-line>" 2
[ 2155s] # 1 "/tmp/petsc-orq54ye3/config.headers/conftest.c"
[ 2155s] # 1 "/tmp/petsc-orq54ye3/config.headers/confdefs.h" 1
[ 2155s] # 2 "/tmp/petsc-orq54ye3/config.headers/conftest.c" 2
[ 2155s] # 1 "/tmp/petsc-orq54ye3/config.headers/conffix.h" 1
[ 2155s] # 3 "/tmp/petsc-orq54ye3/config.headers/conftest.c" 2
[ 2155s] stderr:
[ 2155s] /tmp/petsc-orq54ye3/config.headers/conftest.c:3:10: fatal error: dos.h: No such file or directory
[ 2155s]     3 | #include <dos.h>
[ 2155s]       |          ^~~~~~~
[ 2155s] compilation terminated.
[ 2155s] Source:
[ 2155s] #include "confdefs.h"


spirv-tools
[ 3149s] In file included from /usr/include/string.h:535,
[ 3149s]                  from /usr/include/c++/12/cstring:42,
[ 3149s]                  from /usr/src/packages/BUILD/source/util/bitutils.h:20,
[ 3149s]                  from /usr/src/packages/BUILD/source/util/hex_float.h:27,
[ 3149s]                  from /usr/src/packages/BUILD/source/opt/constants.h:29,
[ 3149s]                  from /usr/src/packages/BUILD/source/opt/ir_context.h:31,
[ 3149s]                  from /usr/src/packages/BUILD/source/opt/amd_ext_to_khr.h:18,
[ 3149s]                  from /usr/src/packages/BUILD/source/opt/amd_ext_to_khr.cpp:15:
[ 3149s] In function 'void* memcpy(void*, const void*, size_t)',
[ 3149s]     inlined from 'void spvtools::opt::IRContext::AddExtension(const std::string&)' at /usr/src/packages/BUILD/source/opt/ir_context.h:1023:14:
[ 3149s] /usr/include/riscv64-linux-gnu/bits/string_fortified.h:29:33: error: 'void* __builtin_memcpy(void*, const void*, long unsigned int)' specified bound between 18446744073709551612 and 18446744073709551615 exceeds maximum object size 9223372036854775807 [-Werror=stringop-overflow=]
[ 3149s]    29 |   return __builtin___memcpy_chk (__dest, __src, __len,
[ 3149s]       |          ~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~
[ 3149s]    30 |                                  __glibc_objsize0 (__dest));
[ 3149s]       |                                  ~~~~~~~~~~~~~~~~~~~~~~~~~~
[ 3170s] cc1plus: all warnings being treated as errors


systemtap
[ 1566s] g++ -DHAVE_CONFIG_H -I.  -DBINDIR='"/usr/bin"' -DSYSCONFDIR='"/etc"' -DPKGDATADIR='"/usr/share/systemtap"' -DPKGLIBDIR='"/usr/lib/systemtap"' -DLOCALEDIR='"/usr/share/locale"' -DDOCDIR='"/usr/share/doc/systemtap"' -DPYEXECDIR='""' -DPY3EXECDIR='""' -I./includes -I./includes/sys -DSTAP_SDT_V2 -D_REENTRANT -I/usr/include/nss -I/usr/include/nspr -Wdate-time -D_FORTIFY_SOURCE=2 -Wall -Wextra -Werror -D_REENTRANT -I/usr/include/nss -I/usr/include/nspr -fstack-protector-all -D_FORTIFY_SOURCE=2 -g -O2 -ffile-prefix-map=/usr/src/packages/BUILD=. -fstack-protector-strong -Wformat -Werror=format-security -c -o stap-elaborate.o `test -f 'elaborate.cxx' || echo './'`elaborate.cxx
[ 1569s] g++ -DHAVE_CONFIG_H -I.  -DBINDIR='"/usr/bin"' -DSYSCONFDIR='"/etc"' -DPKGDATADIR='"/usr/share/systemtap"' -DPKGLIBDIR='"/usr/lib/systemtap"' -DLOCALEDIR='"/usr/share/locale"' -DDOCDIR='"/usr/share/doc/systemtap"' -DPYEXECDIR='""' -DPY3EXECDIR='""' -I./includes -I./includes/sys -DSTAP_SDT_V2 -D_REENTRANT -I/usr/include/nss -I/usr/include/nspr -Wdate-time -D_FORTIFY_SOURCE=2 -Wall -Wextra -Werror -D_REENTRANT -I/usr/include/nss -I/usr/include/nspr -fstack-protector-all -D_FORTIFY_SOURCE=2 -g -O2 -ffile-prefix-map=/usr/src/packages/BUILD=. -fstack-protector-strong -Wformat -Werror=format-security -c -o stap-translate.o `test -f 'translate.cxx' || echo './'`translate.cxx
[ 1736s] g++ -DHAVE_CONFIG_H -I.  -DBINDIR='"/usr/bin"' -DSYSCONFDIR='"/etc"' -DPKGDATADIR='"/usr/share/systemtap"' -DPKGLIBDIR='"/usr/lib/systemtap"' -DLOCALEDIR='"/usr/share/locale"' -DDOCDIR='"/usr/share/doc/systemtap"' -DPYEXECDIR='""' -DPY3EXECDIR='""' -I./includes -I./includes/sys -DSTAP_SDT_V2 -D_REENTRANT -I/usr/include/nss -I/usr/include/nspr -Wdate-time -D_FORTIFY_SOURCE=2 -Wall -Wextra -Werror -D_REENTRANT -I/usr/include/nss -I/usr/include/nspr -fstack-protector-all -D_FORTIFY_SOURCE=2 -g -O2 -ffile-prefix-map=/usr/src/packages/BUILD=. -fstack-protector-strong -Wformat -Werror=format-security -c -o stap-tapsets.o `test -f 'tapsets.cxx' || echo './'`tapsets.cxx
[ 1750s] g++ -DHAVE_CONFIG_H -I.  -DBINDIR='"/usr/bin"' -DSYSCONFDIR='"/etc"' -DPKGDATADIR='"/usr/share/systemtap"' -DPKGLIBDIR='"/usr/lib/systemtap"' -DLOCALEDIR='"/usr/share/locale"' -DDOCDIR='"/usr/share/doc/systemtap"' -DPYEXECDIR='""' -DPY3EXECDIR='""' -I./includes -I./includes/sys -DSTAP_SDT_V2 -D_REENTRANT -I/usr/include/nss -I/usr/include/nspr -Wdate-time -D_FORTIFY_SOURCE=2 -Wall -Wextra -Werror -D_REENTRANT -I/usr/include/nss -I/usr/include/nspr -fstack-protector-all -D_FORTIFY_SOURCE=2 -g -O2 -ffile-prefix-map=/usr/src/packages/BUILD=. -fstack-protector-strong -Wformat -Werror=format-security -c -o stap-buildrun.o `test -f 'buildrun.cxx' || echo './'`buildrun.cxx
[ 1805s] g++ -DHAVE_CONFIG_H -I.  -DBINDIR='"/usr/bin"' -DSYSCONFDIR='"/etc"' -DPKGDATADIR='"/usr/share/systemtap"' -DPKGLIBDIR='"/usr/lib/systemtap"' -DLOCALEDIR='"/usr/share/locale"' -DDOCDIR='"/usr/share/doc/systemtap"' -DPYEXECDIR='""' -DPY3EXECDIR='""' -I./includes -I./includes/sys -DSTAP_SDT_V2 -D_REENTRANT -I/usr/include/nss -I/usr/include/nspr -Wdate-time -D_FORTIFY_SOURCE=2 -Wall -Wextra -Werror -D_REENTRANT -I/usr/include/nss -I/usr/include/nspr -fstack-protector-all -D_FORTIFY_SOURCE=2 -g -O2 -ffile-prefix-map=/usr/src/packages/BUILD=. -fstack-protector-strong -Wformat -Werror=format-security -c -o stap-loc2stap.o `test -f 'loc2stap.cxx' || echo './'`loc2stap.cxx
[ 1870s] g++ -DHAVE_CONFIG_H -I.  -DBINDIR='"/usr/bin"' -DSYSCONFDIR='"/etc"' -DPKGDATADIR='"/usr/share/systemtap"' -DPKGLIBDIR='"/usr/lib/systemtap"' -DLOCALEDIR='"/usr/share/locale"' -DDOCDIR='"/usr/share/doc/systemtap"' -DPYEXECDIR='""' -DPY3EXECDIR='""' -I./includes -I./includes/sys -DSTAP_SDT_V2 -D_REENTRANT -I/usr/include/nss -I/usr/include/nspr -Wdate-time -D_FORTIFY_SOURCE=2 -Wall -Wextra -Werror -D_REENTRANT -I/usr/include/nss -I/usr/include/nspr -fstack-protector-all -D_FORTIFY_SOURCE=2 -g -O2 -ffile-prefix-map=/usr/src/packages/BUILD=. -fstack-protector-strong -Wformat -Werror=format-security -c -o stap-hash.o `test -f 'hash.cxx' || echo './'`hash.cxx
[ 1898s] gcc -DHAVE_CONFIG_H -I.  -DBINDIR='"/usr/bin"' -DSYSCONFDIR='"/etc"' -DPKGDATADIR='"/usr/share/systemtap"' -DPKGLIBDIR='"/usr/lib/systemtap"' -DLOCALEDIR='"/usr/share/locale"' -DDOCDIR='"/usr/share/doc/systemtap"' -DPYEXECDIR='""' -DPY3EXECDIR='""' -I./includes -I./includes/sys -DSTAP_SDT_V2 -D_REENTRANT -I/usr/include/nss -I/usr/include/nspr -Wdate-time -D_FORTIFY_SOURCE=2 -D_GNU_SOURCE -fexceptions -Wall -Wextra -Werror -Wunused -Wformat=2 -W -I/usr/include/nss -I/usr/include/nspr -DSTAP -fstack-protector-all -D_FORTIFY_SOURCE=2 -g -O2 -ffile-prefix-map=/usr/src/packages/BUILD=. -fstack-protector-strong -Wformat -Werror=format-security -c -o stap-mdfour.o `test -f 'mdfour.c' || echo './'`mdfour.c
[ 1902s] g++ -DHAVE_CONFIG_H -I.  -DBINDIR='"/usr/bin"' -DSYSCONFDIR='"/etc"' -DPKGDATADIR='"/usr/share/systemtap"' -DPKGLIBDIR='"/usr/lib/systemtap"' -DLOCALEDIR='"/usr/share/locale"' -DDOCDIR='"/usr/share/doc/systemtap"' -DPYEXECDIR='""' -DPY3EXECDIR='""' -I./includes -I./includes/sys -DSTAP_SDT_V2 -D_REENTRANT -I/usr/include/nss -I/usr/include/nspr -Wdate-time -D_FORTIFY_SOURCE=2 -Wall -Wextra -Werror -D_REENTRANT -I/usr/include/nss -I/usr/include/nspr -fstack-protector-all -D_FORTIFY_SOURCE=2 -g -O2 -ffile-prefix-map=/usr/src/packages/BUILD=. -fstack-protector-strong -Wformat -Werror=format-security -c -o stap-cache.o `test -f 'cache.cxx' || echo './'`cache.cxx
[ 1930s] g++ -DHAVE_CONFIG_H -I.  -DBINDIR='"/usr/bin"' -DSYSCONFDIR='"/etc"' -DPKGDATADIR='"/usr/share/systemtap"' -DPKGLIBDIR='"/usr/lib/systemtap"' -DLOCALEDIR='"/usr/share/locale"' -DDOCDIR='"/usr/share/doc/systemtap"' -DPYEXECDIR='""' -DPY3EXECDIR='""' -I./includes -I./includes/sys -DSTAP_SDT_V2 -D_REENTRANT -I/usr/include/nss -I/usr/include/nspr -Wdate-time -D_FORTIFY_SOURCE=2 -Wall -Wextra -Werror -D_REENTRANT -I/usr/include/nss -I/usr/include/nspr -fstack-protector-all -D_FORTIFY_SOURCE=2 -g -O2 -ffile-prefix-map=/usr/src/packages/BUILD=. -fstack-protector-strong -Wformat -Werror=format-security -c -o stap-util.o `test -f 'util.cxx' || echo './'`util.cxx
[ 1940s] util.cxx: In function 'void ltrim(std::string&)':
[ 1940s] util.cxx:1764:56: error: 'std::pointer_to_unary_function<_Arg, _Result> std::ptr_fun(_Result (*)(_Arg)) [with _Arg = int; _Result = int]' is deprecated: use 'std::function' instead [-Werror=deprecated-declarations]
[ 1940s]  1764 |                        std::not1(std::ptr_fun<int, int>(std::isspace))));
[ 1940s]       |                                  ~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~
[ 1940s] In file included from /usr/include/c++/12/string:48,
[ 1940s]                  from util.h:8,
[ 1940s]                  from util.cxx:17:


tpm2-tss
[ 1040s] configure:5886: checking for unistd.h
[ 1040s] configure:5886: gcc -c -g -O2 -ffile-prefix-map=/usr/src/packages/BUILD=. -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 conftest.c >&5
[ 1040s] configure:5886: $? = 0
[ 1040s] configure:5886: result: yes
[ 1040s] configure:5886: checking for wchar.h
[ 1040s] configure:5886: gcc -c -g -O2 -ffile-prefix-map=/usr/src/packages/BUILD=. -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 conftest.c >&5
[ 1040s] configure:5886: $? = 0
[ 1040s] configure:5886: result: yes
[ 1040s] configure:5886: checking for minix/config.h
[ 1040s] configure:5886: gcc -c -g -O2 -ffile-prefix-map=/usr/src/packages/BUILD=. -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 conftest.c >&5
[ 1040s] conftest.c:50:10: fatal error: minix/config.h: No such file or directory
[ 1040s]    50 | #include <minix/config.h>
[ 1040s]       |          ^~~~~~~~~~~~~~~~
[ 1040s] compilation terminated.
[ 1040s] configure:5886: $? = 1
[ 1040s] configure: failed program was:




编译错误包总共有：
9


