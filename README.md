# unitop

`unitop` is a universal per-process bandwidth monitoring tool that precisely monitors low-level TCP/IP system calls in the Linux kernel and measures the bandwidth. It is an extended version of `tcptop` which is available in BCC toolchain.
Most available tools use `/proc/net` to gather information. However, these applications have problems in distinguishing different processes, especially in UDP traffics.  

## Installation
To use `unitop`, the BCC should be installed in the host. Please follow the installation guide in [BCC](https://github.com/iovisor/bcc/blob/master/INSTALL.md) official page.
On systems (As I tested on Nvidia Xavier) the `BCC` collection is not enough. So the `python3-bpfcc` also should be installed via `apt`:
```bash
$ sudo apt install python3-bpfcc
``` 
## Usage
Simply run with root right privilege. 

```bash
$ sudo ./unitop
```
## Sample output
```bash
13:59:59 loadavg: 6.37 4.47 3.36 2/1414 104511

PID    COMM         LADDR                 RADDR                 RX_KiB TX_KiB
15010  chrome       192.168.1.12:46654    79.127.127.21:443       6840      0
15010  chrome       192.168.1.12:40338    185.166.104.3:443          0      0
15010  chrome       192.168.1.12:41590    185.166.104.4:443          0      0
```
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)