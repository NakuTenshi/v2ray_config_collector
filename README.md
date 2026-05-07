# v2ray config collector
<a href="https://github.com/NakuTenshi/v2ray_config_collector/blob/main/README_FA.md">فارسی</a>


the ```collect.py``` is a script python that collects v2ray configs from gived ```raw.githubusercontent.com``` sources and test them with TCP handshake

## how to use
first of all you need to clone this repository:

```bash
git clone https://github.com/NakuTenshi/v2ray_config_collector ; 
cd v2ray_config_collector
```

then you need to install the scirpt's **requirements**:

``` bash 
pip3 install -r requirements.txt
```

after all you can easily run the script by:

```bash
python3 collect.py
```
enjoy



## Note

> the ``` sources.txt ``` must be root directory with ```collect.py``` script file

> If you wish to include additional sources for verification, you can easily add them to the ``` sources.txt ``` file.

> the ``` raw_sources.txt ``` file is for those sources that i didn't validate them yet


## tips 

after collecting the configs may be more than 1000 and be difficult to paste it to mobile version of v2ray,
you can split the ``` ./configs/configs.txt ``` file with this command:

```bash
split -l 1000 -d --additional-suffix=.txt configs.txt config_
```
the output will be somthing like this:

```text 
config_00.txt  config_01.txt  config_02.txt  config_03.txt
  ```
