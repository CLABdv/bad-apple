PROJECT = bad-apple
BUILD_DIR = bin

SHARED_DIR = ../common
CFILES = main.c
CFILES += lcd.c clock.c sdram.c cdcacm.c

# TODO - you will need to edit these two lines!
DEVICE=stm32f429zit6
OOCD_FILE = board/stm32f4discovery.cfg

# You shouldn't have to edit anything below here.
VPATH += $(SHARED_DIR)
INCLUDES += $(patsubst %,-I%, . $(SHARED_DIR))
OPENCM3_DIR=../libopencm3

include $(OPENCM3_DIR)/mk/genlink-config.mk
include ../rules.mk
include $(OPENCM3_DIR)/mk/genlink-rules.mk
