Name     : golang-github-kisielk-errcheck
Version  : aa69c6199800e8aeeedf51950f830458e4cb73e3
Release  : 3
URL      : https://github.com/kisielk/errcheck/archive/aa69c6199800e8aeeedf51950f830458e4cb73e3.tar.gz
Source0  : https://github.com/kisielk/errcheck/archive/aa69c6199800e8aeeedf51950f830458e4cb73e3.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : go
BuildRequires : golang-googlecode-go-tools
BuildRequires : golang-github-kisielk-gotool

%description
# errcheck
errcheck is a program for checking for unchecked errors in go programs.

%prep
%setup -q -n errcheck-aa69c6199800e8aeeedf51950f830458e4cb73e3

%build
export LANG=C
mkdir -p build-dir/src/github.com/kisielk
ln -s $(pwd) build-dir/src/github.com/kisielk/errcheck
export GOPATH=$(pwd)/build-dir:/usr/lib/golang
pushd build-dir
    go build github.com/kisielk/errcheck
popd

%install
gopath="/usr/lib/golang"
library_path="github.com/kisielk/errcheck"
rm -rf %{buildroot}
install -d -p %{buildroot}${gopath}/src/${library_path}/
for file in $(find . -iname "*.go" -o -iname "*.h" -o -iname "*.c") ; do
     echo ${file}
     install -d -p %{buildroot}${gopath}/src/${library_path}/$(dirname $file)
     cp -pav $file %{buildroot}${gopath}/src/${library_path}/$file
done

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
gopath="/usr/lib/golang"
export GOPATH="%{buildroot}${gopath}"
go test -v -x github.com/kisielk/errcheck

%files
%defattr(-,root,root,-)
/usr/lib/golang/src/github.com/kisielk/errcheck/internal/errcheck/errcheck.go
/usr/lib/golang/src/github.com/kisielk/errcheck/internal/errcheck/errcheck_test.go
/usr/lib/golang/src/github.com/kisielk/errcheck/main.go
/usr/lib/golang/src/github.com/kisielk/errcheck/main_test.go
/usr/lib/golang/src/github.com/kisielk/errcheck/testdata/main.go
/usr/lib/golang/src/github.com/kisielk/errcheck/testdata/main2.go
