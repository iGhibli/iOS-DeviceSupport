# iOS-DeviceSupport

This repository holds the device support files for the iOS, and I will update it regularly.

## Usage

See docs: [https://ighibli.github.io/2017/03/28/Could-not-locate-device-support-files/](https://ighibli.github.io/2017/03/28/Could-not-locate-device-support-files/)

Below command will try to unzip all new device support files to `/Applications/Xcode.app`.

```sh
sudo ./deploy.py
```

You can use `-t` if your Xcode is not in `/Applications/` or has different name.

```sh
sudo ./deploy.py -t /Applications/Xcode\ 9.app
```

```sh
./deploy.py -h
usage: deploy.py [-h] [-t TARGET]

optional arguments:
  -h, --help  show this help message and exit
  -t TARGET   The path for Xcode
```

## Supported versions

1. iOS8
   * 8.0 `2017/04/07`
   * 8.1 `2017/04/07`
   * 8.2 `2017/04/07`
   * 8.3 `2017/04/07`
   * 8.4 `2017/04/07`
2. iOS9
   * 9.0 `2017/04/07`
   * 9.1 `2017/04/07`
   * 9.2 `2017/04/07`
   * 9.3 `2017/04/07`
3. iOS10
   * 10.0 (14A345) `2017/04/07`
   * 10.0 `2017/12/05`
   * 10.1 (14B72) `2017/04/07`
   * 10.1 `2017/12/05`
   * 10.2 (14C92) `2017/04/07`
   * 10.2 `2017/12/05`
   * 10.3 (14E269) `2017/04/07`
   * 10.3 `2017/12/05`
4. iOS11
   * 11.0 `2017/12/05`
   * 11.1 (15B87) `2017/12/05`
   * 11.1 `2017/12/11`
   * 11.2 (15C107) `2017/12/11`
   * 11.2 `2018/03/06`
   * 11.3 (15E5167d) `2018/01/30`
   * 11.3 (15E5201e) `2018/03/06`
   * 11.3 `2018/04/09`
   * 11.4 (15F5037c) `2018/04/09`
   * 11.4 (15F5061c) `2018/07/29`
   * 11.4 (15F79) `2018/07/29`
   * 11.4 `2018/06/07`
5. iOS12
   * 12.0 (16A5288q) `2018/06/07`
   * 12.0 (16A5308d) `2018/06/19`
   * 12.0 (16A5318d) `2018/06/29`
   * 12.0 (16A5327d) `2018/07/20`
   * 12.0 (16A5339e) `2018/07/31`
   * 12.0 (16A5354b) `2018/08/15`
   * 12.0 (16A366) `2018/09/18`
   * 12.0 `2019/01/29`
   * 12.1 (16B5059d) `2018/09/21`
   * 12.1 (16B5068g) `2018/10/08`
   * 12.1 (16B5084a) `2018/10/16`
   * 12.1 (16B91) `2018/10/31`
   * 12.1 (16B5084a) `2018/10/16`
   * 12.1 `2019/01/29`
   * 12.2 (16E5181e) `2019/01/29`
   * 12.2 (16E5212e) `2019/03/07`
   * 12.2 (16E226) `2019/03/27`
   * 12.3 `2019/06/04`
   * 12.4 (16G73) `2019/07/22`
   * 12.4 (FromXcode_11_Beta_7_xip) `2019/09/03`
6. iOS13
   * 13.0 `2019/06/04`
   * 13.0 (FromXcode_11_Beta_7_xip) `2019/09/03`
   * 13.1 `2019/08/28`
   * 13.2 `2019/10/02`
   * 13.2 (FromXcode_11.2.1_GM_Seed) `2019/11/11`
   * 13.2 (FromXcode11.2.1(11B500)) `2019/11/15`
