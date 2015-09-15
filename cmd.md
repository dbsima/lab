# prints the names of all files recursively whose MIME type is a video type.
find . -type f -exec file -N -i -- {} + | sed -n 's!: video/[^:]*$!!p'


### Graphical card

## Remove nvidia*
sudo apt-get remove --purge nvidia-*

## Install Bumblebee Ubuntu 14.04

sudo apt-get install bumblebee bumblebee-nvidia primus nvidia-331

sudo apt-get install python-appindicator

git clone https://github.com/Bumblebee-Project/bumblebee-ui.git
cd bumblebee-ui
sudo ./INSTALL

# Go to Startup Applications and add 'bumblebee-indicator'

# Now reboot


### Memory


# Maximum supported
$ sudo dmidecode -t 16
# dmidecode 2.12
SMBIOS 2.7 present.

Handle 0x001B, DMI type 16, 23 bytes
Physical Memory Array
	Location: System Board Or Motherboard
	Use: System Memory
	Error Correction Type: None
	Maximum Capacity: 16 GB
	Error Information Handle: No Error
	Number Of Devices: 2


# Currently installed
$ sudo dmidecode -t 17
# dmidecode 2.12
SMBIOS 2.7 present.

Handle 0x001C, DMI type 17, 34 bytes
Memory Device
	Array Handle: 0x001B
	Error Information Handle: 0x001E
	Total Width: 64 bits
	Data Width: 64 bits
	Size: 4096 MB
	Form Factor: SODIMM
	Set: None
	Locator: ChannelA-DIMM0
	Bank Locator: BANK 0
	Type: DDR3
	Type Detail: Synchronous
	Speed: 1333 MHz
	Manufacturer: Kinston
	Serial Number: 742033A6
	Asset Tag: 0123456789
	Part Number: ACR512X64D3S13C9G
	Rank: Unknown
	Configured Clock Speed: 1333 MHz

Handle 0x0020, DMI type 17, 34 bytes
Memory Device
	Array Handle: 0x001B
	Error Information Handle: Not Provided
	Total Width: Unknown
	Data Width: Unknown
	Size: No Module Installed
	Form Factor: DIMM
	Set: None
	Locator: ChannelA-DIMM1
	Bank Locator: BANK 1
	Type: Unknown
	Type Detail: None
	Speed: Unknown
	Manufacturer: Not Specified
	Serial Number: Not Specified
	Asset Tag: 0123456789
	Part Number: Not Specified
	Rank: Unknown
	Configured Clock Speed: Unknown

Handle 0x0022, DMI type 17, 34 bytes
Memory Device
	Array Handle: 0x001B
	Error Information Handle: 0x0024
	Total Width: 64 bits
	Data Width: 64 bits
	Size: 4096 MB
	Form Factor: SODIMM
	Set: None
	Locator: ChannelB-DIMM0
	Bank Locator: BANK 2
	Type: DDR3
	Type Detail: Synchronous
	Speed: 1333 MHz
	Manufacturer: Kinston
	Serial Number: EE3631A5
	Asset Tag: 0123456789
	Part Number: 99U5428-055.A00G
	Rank: Unknown
	Configured Clock Speed: 1333 MHz

Handle 0x0026, DMI type 17, 34 bytes
Memory Device
	Array Handle: 0x001B
	Error Information Handle: Not Provided
	Total Width: Unknown
	Data Width: Unknown
	Size: No Module Installed
	Form Factor: DIMM
	Set: None
	Locator: ChannelB-DIMM1
	Bank Locator: BANK 3
	Type: Unknown
	Type Detail: None
	Speed: Unknown
	Manufacturer: Not Specified
	Serial Number: Not Specified
	Asset Tag: 0123456789
	Part Number: Not Specified
	Rank: Unknown
	Configured Clock Speed: Unknown
