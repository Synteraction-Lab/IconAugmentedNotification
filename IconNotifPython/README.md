# IconNotifPython
Trigger icon-augmented notfications on OHMDs (Epson BT300). 



## Installation
- make sure python3 is installed
- install `conda` (e.g., [Anaconda](https://docs.anaconda.com/anaconda/install/)/[Miniconda](https://docs.conda.io/en/latest/miniconda.html))
- create new conda environment, `conda env create -n psychopy -f psychopy-env.yml`
- activate `psychopy` environment, `conda activate psychopy`
- [only if demos are not working] downgrade `xlrd` version, `pip install xlrd==1.2.0`



### OHMD (Android) app
- install the corresponding OHMD app in [NIPGlass](https://github.com/NUS-HCILab/NIPGlass) to the hardware (e.g., Epson BT-300 or any Android device) 
- e.g. if you want to try `illustrations_0.x` branch of this repo, you need to install `notification_illustrations_0.x` brach of `NIPGlass` repo
    - if you can not find the exact number use the latest version (e.g. [illustrations_0.2](https://github.com/NUS-HCILab/TriggerNotificationPython/tree/poc/illustrations_0.2) -> [notification_illustrations_0.1](https://github.com/NUS-HCILab/NIPGlass/tree/poc/notification_illustrations_0.1))


## Run the application
- edit [device_config.py](device_config.py) and set the IP address of the OHMD
- run the `python task_vigilance.py` (or `trigger.sh` in terminal) and input the <participant_id> (default: p0) and <session_id> (default: 0) when prompts
- see the configurations at [participant_config.py](participant_config.py)
- all data will be logged to `data/<participant_id>`
