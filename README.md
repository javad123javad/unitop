# unitop

`unitop` is a universal per-process bandwidth monitoring tool that precisely monitors low-level TCP/IP system calls in the Linux kernel and measures the bandwidth. It is an extended version of `tcptop` which is available in BCC toolchain.
Most available tools use `/proc/net` to gather information. However, these applications have problems in distinguishing different processes, especially in UDP traffics.  

## Installation
To use `unitop`, the BCC should be installed in the host. Please follow the installation guide in [BCC](https://github.com/iovisor/bcc/blob/master/INSTALL.md) official page.
## Usage
Simply run with root right privilege. 

```bash
$ sudo ./unitop
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)