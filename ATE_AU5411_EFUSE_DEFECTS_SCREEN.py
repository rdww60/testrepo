### [VT_TRACKING_NUMBER]: A0_AU5411_6_1 (ATE_AU5411_EFUSE_DEFECTS_SCREEN)
### Chip Configuration time 0.003400 s
'''
#######################################################################################################
###################### This code is to perform EFUSE_DEFECTS_SCREEN ###################################
#######################################################################################################
###Note:
###                     - means All are comments
#                       - Will be removed to use this code to test with Python
#i2c.i2cw               - I2c write operation
#i2c.i2cr               - I2c read operation
#time.sleep(X)          - Represents 'X' seconds wait time
#if(glob.bench_char)    - Only needed for bench char. Need to be neglected in ATE
#######################################################################################################
ATE_CONNECTORS:
   1- GND    : TESTER GROUND INTERFACE [ 0.000 ]
   2- VI80   : TESTER SUPPLY INTERFACE [ x.xxx ]
   3- XTAL   : CRYSTAL OSCILLATOR      [ 25MHZ ]
   4- UP1600 : GPIO INTERFACE
               - HIZ                   [ ----- ]
               - I2C MASTER            [ SCL, SDA ]
               - MEASURE               [ VOLTAGE, CURRENT ]
               - VSOURCE               [ VDD, GND ]
               - ISOURCE               [ SOURCE, SINK ]


DESCRIPTION:

NOTE: I2C FREQUENCY = 400KHz

STEP_1 [POWER UP] STATIC CONDITION
   --------------------------------------------------------------------------
   NUMBER : NAME                        :  VALUE   :  ATE_CONN :  MODE(AC/DC)
   --------------------------------------------------------------------------
     15   : VCC                         :  3.465V  :  VI80     :  NA
     42   : VCC1                        :  3.465V  :  VI80     :  NA
     05   : VCCOA_1                     :  3.465V  :  VI80     :  NA
     08   : VCCOA_2                     :  3.465V  :  VI80     :  NA
     29   : VCCOB_1                     :  3.465V  :  VI80     :  NA
     32   : VCCOB_2                     :  3.465V  :  VI80     :  NA
     45   : VCCOC                       :  3.465V  :  VI80     :  NA
   --------------------------------------------------------------------------
     13   : GND_1                       :  0.000   :  GND      :  NA
     18   : GND_2                       :  0.000   :  GND      :  NA
     24   : GND_3                       :  0.000   :  GND      :  NA
     43   : GND_4                       :  0.000   :  GND      :  NA
     48   : GND_5                       :  0.000   :  GND      :  NA
   --------------------------------------------------------------------------
     22   : CLKIN_SEL1_SCAN_RESET       :  GND     :  UP1600   :  VSOURCE
     19   : CLKIN_SEL0_SCAN_IN          :  GND     :  UP1600   :  VSOURCE
     46   : REFOUT_EN_SCAN_OUT_SDAIO    :  SDA     :  UP1600   :  I2C MASTER
     47   : CLKOUTA_TYPE1_SCAN_CLK_SCLK :  SCL     :  UP1600   :  I2C MASTER
     14   : CLKOUTA_TYPE0               :  GND     :  UP1600   :  VSOURCE
     39   : CLKOUTB_TYPE1_DIAG          :  GND     :  UP1600   :  VSOURCE
     23   : CLKOUTB_TYPE0_SCAN_EN       :  GND     :  UP1600   :  VSOURCE
     37   : GND_I2C_EN                  :  VDD     :  UP1600   :  VSOURCE
     38   : TEST_EN                     :  GND     :  UP1600   :  VSOURCE
   --------------------------------------------------------------------------
     16   : OSCIN                       :  25MHz   :  XTAL     :  DC COUPLED
     17   : OSCOUT                      :  25MHz   :  XTAL     :  DC COUPLED
     20   : CLKIN0_P                    :  -----   :  UP1600   :  HIZ
     21   : CLKIN0_N                    :  -----   :  UP1600   :  HIZ
     41   : CLKIN1_P                    :  -----   :  UP1600   :  HIZ
     40   : CLKIN1_N                    :  -----   :  UP1600   :  HIZ
   --------------------------------------------------------------------------
     44   : REFOUT                      :  -----   :  UP1600   :  HIZ
   --------------------------------------------------------------------------
     01   : CLKOUTA0_P                  :  -----   :  UP1600   :  50 Ohms to GND
     02   : CLKOUTA0_N                  :  -----   :  UP1600   :  50 Ohms to GND
     03   : CLKOUTA1_P                  :  -----   :  UP1600   :  50 Ohms to GND
     04   : CLKOUTA1_N                  :  -----   :  UP1600   :  50 Ohms to GND
     06   : CLKOUTA2_P                  :  -----   :  UP1600   :  50 Ohms to GND
     07   : CLKOUTA2_N                  :  -----   :  UP1600   :  50 Ohms to GND
     09   : CLKOUTA3_P                  :  -----   :  UP1600   :  50 Ohms to GND
     10   : CLKOUTA3_N                  :  -----   :  UP1600   :  50 Ohms to GND
     11   : CLKOUTA4_P                  :  -----   :  UP1600   :  50 Ohms to GND
     12   : CLKOUTA4_N                  :  -----   :  UP1600   :  50 Ohms to GND
   --------------------------------------------------------------------------
     36   : CLKOUTB0_P                  :  -----   :  UP1600   :  50 Ohms to GND
     35   : CLKOUTB0_N                  :  -----   :  UP1600   :  50 Ohms to GND
     34   : CLKOUTB1_P                  :  -----   :  UP1600   :  50 Ohms to GND
     33   : CLKOUTB1_N                  :  -----   :  UP1600   :  50 Ohms to GND
     31   : CLKOUTB2_P                  :  -----   :  UP1600   :  50 Ohms to GND
     30   : CLKOUTB2_N                  :  -----   :  UP1600   :  50 Ohms to GND
     28   : CLKOUTB3_P                  :  -----   :  UP1600   :  50 Ohms to GND
     27   : CLKOUTB3_N                  :  -----   :  UP1600   :  50 Ohms to GND
     26   : CLKOUTB4_P                  :  -----   :  UP1600   :  50 Ohms to GND
     25   : CLKOUTB4_N                  :  -----   :  UP1600   :  50 Ohms to GND
   --------------------------------------------------------------------------

STEP_2 [READ ALL EFUSE REGISTERS] 

STEP_3 [COMPARE STEP_2 VALUES WITH SPECIFICATION LIMITS]

STEP_4 [CAPTURE E_PRODUCT_CODE,E_HTOL_EN,E_RC_CODE,E_XO_CAPTRIM1,CAPTRIM_X2,E_XO_AMP_PROG,E_LOCK AND COMPARE WITH SPECIFICATION LIMITS]


SPECIFICATION LIMITS IN BINARY
reg0x10_data          0000X000
reg0x11_data          00000000
reg0x12_data          00000000
reg0x13_data          00000000
reg0x14_data          00000000
reg0x15_data          00000000
reg0x16_data          0X000000
reg0x18_data          XXXXXXXX
reg0x19_data          XXXXXXXX
reg0x1a_data          XXXXXXXX
reg0x1b_data          XXXXXXXX
reg0x1c_data          XXXXXXXX
reg0x1d_data          00000000
reg0x1f_data          00000000
reg0x20_data          XXXXXXXX 
reg0x21_data          XXXXXXXX 
reg0x22_data          XXXXXXXX 
reg0x23_data          XXXXXXXX 
reg0x24_data          XXXXXXXX 
reg0x25_data          00000000
reg0x26_data          00000000
reg0x28_data          00000000
reg0x29_data          00000000
reg0x2a_data          00000000
reg0x2b_data          00000000
reg0x2c_data          0000XXXX
reg0x2d_data          000XX00X
reg0x2e_data          000000X0
reg0x2f_data          000XX00X

E_PRODUCT_CODE        00
E_HTOL_EN             0 or 1
E_RC_CODE             00000 to 1111
E_XO_CAPTRIM1         00000 or 11001
CAPTRIM_X2            00 or 10
E_XO_AMP_PROG         0000 or 1001
E_LOCK                00 or 01
'''


### EXCLUDE THIS FOR ATE ##########################
import glob,time
if glob.bench_char:
    from ATE_INSTRUMENTS_HANDLER import *
### EXCLUDE THIS FOR ATE ##########################


#######################################################################################################
### STEP_1 START


### EXCLUDE THIS FOR ATE ##########################
if glob.bench_char:
    POWER_UP_CONFIG(VDD=3.465,VDDO=3.465,CLKINSEL=0,ODRA=0,ODRB=0,REFOUT_EN=1,I2C_EN=1,TEST_NAME='ATE_EFUSE_DEFECTS_SCREEN')
### EXCLUDE THIS FOR ATE ##########################


### INCLUDE THIS FOR ATE ##########################
time.sleep(0.0005)
### INCLUDE THIS FOR ATE ##########################


#STEP_1 END
#######################################################################################################


#######################################################################################################
### STEP_2 START


### INCLUDE THIS FOR ATE ##########################
i2c.i2cr(0x55,0x10,0xVV)	      #reg0x10_data = 
i2c.i2cr(0x55,0x11,0xVV)	      #reg0x11_data = 
i2c.i2cr(0x55,0x12,0xVV)	      #reg0x12_data = 
i2c.i2cr(0x55,0x13,0xVV)	      #reg0x13_data = 
i2c.i2cr(0x55,0x14,0xVV)	      #reg0x14_data = 
i2c.i2cr(0x55,0x15,0xVV)	      #reg0x15_data = 
i2c.i2cr(0x55,0x16,0xVV)	      #reg0x16_data = 
i2c.i2cr(0x55,0x18,0xVV)	      #reg0x18_data = 
i2c.i2cr(0x55,0x19,0xVV)	      #reg0x19_data = 
i2c.i2cr(0x55,0x1a,0xVV)	      #reg0x1a_data = 
i2c.i2cr(0x55,0x1b,0xVV)	      #reg0x1b_data = 
i2c.i2cr(0x55,0x1c,0xVV)	      #reg0x1c_data = 
i2c.i2cr(0x55,0x1d,0xVV)	      #reg0x1d_data = 
i2c.i2cr(0x55,0x1f,0xVV)	      #reg0x1f_data = 
i2c.i2cr(0x55,0x20,0xVV)	      #reg0x20_data = 
i2c.i2cr(0x55,0x21,0xVV)	      #reg0x21_data = 
i2c.i2cr(0x55,0x22,0xVV)	      #reg0x22_data = 
i2c.i2cr(0x55,0x23,0xVV)	      #reg0x23_data = 
i2c.i2cr(0x55,0x24,0xVV)	      #reg0x24_data = 
i2c.i2cr(0x55,0x25,0xVV)	      #reg0x25_data = 
i2c.i2cr(0x55,0x26,0xVV)	      #reg0x26_data = 
i2c.i2cr(0x55,0x28,0xVV)	      #reg0x28_data = 
i2c.i2cr(0x55,0x29,0xVV)	      #reg0x29_data = 
i2c.i2cr(0x55,0x2a,0xVV)	      #reg0x2a_data = 
i2c.i2cr(0x55,0x2b,0xVV)	      #reg0x2b_data = 
i2c.i2cr(0x55,0x2c,0xVV)	      #reg0x2c_data = 
i2c.i2cr(0x55,0x2d,0xVV)	      #reg0x2d_data = 
i2c.i2cr(0x55,0x2e,0xVV)	      #reg0x2e_data = 
i2c.i2cr(0x55,0x2f,0xVV)	      #reg0x2f_data = 

### i2c.i2cr(0x55,0x10)	      #reg0x10_data = 
### i2c.i2cr(0x55,0x11)	      #reg0x11_data = 
### i2c.i2cr(0x55,0x12)	      #reg0x12_data = 
### i2c.i2cr(0x55,0x13)	      #reg0x13_data = 
### i2c.i2cr(0x55,0x14)	      #reg0x14_data = 
### i2c.i2cr(0x55,0x15)	      #reg0x15_data = 
### i2c.i2cr(0x55,0x16)	      #reg0x16_data = 
### i2c.i2cr(0x55,0x18)	      #reg0x18_data = 
### i2c.i2cr(0x55,0x19)	      #reg0x19_data = 
### i2c.i2cr(0x55,0x1a)	      #reg0x1a_data = 
### i2c.i2cr(0x55,0x1b)	      #reg0x1b_data = 
### i2c.i2cr(0x55,0x1c)	      #reg0x1c_data = 
### i2c.i2cr(0x55,0x1d)	      #reg0x1d_data = 
### i2c.i2cr(0x55,0x1f)	      #reg0x1f_data = 
### i2c.i2cr(0x55,0x20)	      #reg0x20_data = 
### i2c.i2cr(0x55,0x21)	      #reg0x21_data = 
### i2c.i2cr(0x55,0x22)	      #reg0x22_data = 
### i2c.i2cr(0x55,0x23)	      #reg0x23_data = 
### i2c.i2cr(0x55,0x24)	      #reg0x24_data = 
### i2c.i2cr(0x55,0x25)	      #reg0x25_data = 
### i2c.i2cr(0x55,0x26)	      #reg0x26_data = 
### i2c.i2cr(0x55,0x28)	      #reg0x28_data = 
### i2c.i2cr(0x55,0x29)	      #reg0x29_data = 
### i2c.i2cr(0x55,0x2a)	      #reg0x2a_data = 
### i2c.i2cr(0x55,0x2b)	      #reg0x2b_data = 
### i2c.i2cr(0x55,0x2c)	      #reg0x2c_data = 
### i2c.i2cr(0x55,0x2d)	      #reg0x2d_data = 
### i2c.i2cr(0x55,0x2e)	      #reg0x2e_data = 
### i2c.i2cr(0x55,0x2f)	      #reg0x2f_data = 
### INCLUDE THIS FOR ATE ##########################


### STEP_2 END
#######################################################################################################


#######################################################################################################
### STEP_3 START


### INCLUDE THIS FOR ATE ##########################
### COMPARE STEP_2 VALUES WITH SPECIFICATION LIMITS
### INCLUDE THIS FOR ATE ##########################


### EXCLUDE THIS FOR ATE ##########################
if glob.bench_char:
    EDS_FILEWRITE(0x10,0x00,0x08,reg0x10_data)
    EDS_FILEWRITE(0x11,0x00,0x00,reg0x11_data)
    EDS_FILEWRITE(0x12,0x00,0x00,reg0x12_data)
    EDS_FILEWRITE(0x13,0x00,0x00,reg0x13_data)
    EDS_FILEWRITE(0x14,0x00,0x00,reg0x14_data)
    EDS_FILEWRITE(0x15,0x00,0x00,reg0x15_data)
    EDS_FILEWRITE(0x16,0x00,0x40,reg0x16_data)
    EDS_FILEWRITE(0x1d,0x00,0x00,reg0x1d_data)
    EDS_FILEWRITE(0x1f,0x00,0x00,reg0x1f_data)
    EDS_FILEWRITE(0x25,0x00,0x00,reg0x25_data)
    EDS_FILEWRITE(0x26,0x00,0x00,reg0x26_data)
    EDS_FILEWRITE(0x28,0x00,0x00,reg0x28_data)
    EDS_FILEWRITE(0x29,0x00,0x00,reg0x29_data)
    EDS_FILEWRITE(0x2a,0x00,0x00,reg0x2a_data)
    EDS_FILEWRITE(0x2b,0x00,0x00,reg0x2b_data)
    EDS_FILEWRITE(0x2c,0x00,0x08,reg0x2c_data)
    EDS_FILEWRITE(0x2d,0x00,0x19,reg0x2d_data)
    EDS_FILEWRITE(0x2e,0x00,0x02,reg0x2e_data)
    EDS_FILEWRITE(0x2f,0x00,0x19,reg0x2f_data)
### EXCLUDE THIS FOR ATE ##########################


### STEP_3 END
#######################################################################################################


#######################################################################################################
### STEP_4 START


### INCLUDE THIS FOR ATE ##########################
### CHECK DEFAULT EFUSE VALUES OF EFUSE 
### [CAPTURE E_PRODUCT_CODE]
E_PRODUCT_CODE = (reg0x10_data & 0x18) >> 3
### [CAPTURE E_HTOL_EN]
E_HTOL_EN = (reg0x16_data & 0x40) >> 6
### [CAPTURE E_RCAL_CODE_A0 AND E_RPOLY_CODE_A0]
E_RCAL_CODE_A0 = reg0x18_data >> 4
E_RPOLY_CODE_A0 = reg0x18_data & 0x0f
### [CAPTURE E_RCAL_CODE_A1 AND E_RPOLY_CODE_A1]
E_RCAL_CODE_A1 = reg0x19_data >> 4
E_RPOLY_CODE_A1 = reg0x19_data & 0x0f
### [CAPTURE E_RCAL_CODE_A2 AND E_RPOLY_CODE_A2]
E_RCAL_CODE_A2 = reg0x1a_data >> 4
E_RPOLY_CODE_A2 = reg0x1a_data & 0x0f
### [CAPTURE E_RCAL_CODE_A3 AND E_RPOLY_CODE_A3]
E_RCAL_CODE_A3 = reg0x1b_data >> 4
E_RPOLY_CODE_A3 = reg0x1b_data & 0x0f
### [CAPTURE E_RCAL_CODE_A4 AND E_RPOLY_CODE_A4]
E_RCAL_CODE_A4 = reg0x1c_data >> 4
E_RPOLY_CODE_A4 = reg0x1c_data & 0x0f
### [CAPTURE E_RCAL_CODE_B0 AND E_RPOLY_CODE_B0]
E_RCAL_CODE_B0 = reg0x20_data >> 4
E_RPOLY_CODE_B0 = reg0x20_data & 0x0f
### [CAPTURE E_RCAL_CODE_B1 AND E_RPOLY_CODE_B1]
E_RCAL_CODE_B1 = reg0x21_data >> 4
E_RPOLY_CODE_B1 = reg0x21_data & 0x0f
### [CAPTURE E_RCAL_CODE_B2 AND E_RPOLY_CODE_B2]
E_RCAL_CODE_B2 = reg0x22_data >> 4
E_RPOLY_CODE_B2 = reg0x22_data & 0x0f
### [CAPTURE E_RCAL_CODE_B3 AND E_RPOLY_CODE_B3]
E_RCAL_CODE_B3 = reg0x23_data >> 4
E_RPOLY_CODE_B3 = reg0x23_data & 0x0f
### [CAPTURE E_RCAL_CODE_B4 AND E_RPOLY_CODE_B4]
E_RCAL_CODE_B4 = reg0x24_data >> 4
E_RPOLY_CODE_B4 = reg0x24_data & 0x0f
### [CAPTURE E_RC_CODE]
E_RC_CODE = reg0x2c_data & 0x0f
### [CAPTURE E_XO_CAPTRIM1]
E_XO_CAPTRIM1 = reg0x2d_data & 0x1f
### [CAPTURE CAPTRIM_X2]
CAPTRIM_X2 = reg0x2e_data & 0x03
### [CAPTUR E_XO_AMP_PROG]
E_XO_AMP_PROG = reg0x2f_data & 0x0F
### [CAPTURE E_LOCK]
E_LOCK = (reg0x2f_data & 0x30) >> 4
### INCLUDE THIS FOR ATE ##########################


### EXCLUDE THIS FOR ATE ##########################
if glob.bench_char:
    EDS_FILEWRITE('E_PRODUCT_CODE',0,1,E_PRODUCT_CODE)
    EDS_FILEWRITE('E_HTOL_EN',0,1,E_HTOL_EN)
    EDS_FILEWRITE('E_RCAL_CODE_A0',0,15,E_RCAL_CODE_A0)
    EDS_FILEWRITE('E_RPOLY_CODE_A0',0,15,E_RPOLY_CODE_A0)
    EDS_FILEWRITE('E_RCAL_CODE_A1',0,15,E_RCAL_CODE_A1)
    EDS_FILEWRITE('E_RPOLY_CODE_A1',0,15,E_RPOLY_CODE_A1)
    EDS_FILEWRITE('E_RCAL_CODE_A2',0,15,E_RCAL_CODE_A2)
    EDS_FILEWRITE('E_RPOLY_CODE_A2',0,15,E_RPOLY_CODE_A2)
    EDS_FILEWRITE('E_RCAL_CODE_A3',0,15,E_RCAL_CODE_A3)
    EDS_FILEWRITE('E_RPOLY_CODE_A3',0,15,E_RPOLY_CODE_A3)
    EDS_FILEWRITE('E_RCAL_CODE_A4',0,15,E_RCAL_CODE_A4)
    EDS_FILEWRITE('E_RPOLY_CODE_A4',0,15,E_RPOLY_CODE_A4)
    EDS_FILEWRITE('E_RCAL_CODE_B0',0,15,E_RCAL_CODE_B0)
    EDS_FILEWRITE('E_RPOLY_CODE_B0',0,15,E_RPOLY_CODE_B0)
    EDS_FILEWRITE('E_RCAL_CODE_B1',0,15,E_RCAL_CODE_B1)
    EDS_FILEWRITE('E_RPOLY_CODE_B1',0,15,E_RPOLY_CODE_B1)
    EDS_FILEWRITE('E_RCAL_CODE_B2',0,15,E_RCAL_CODE_B2)
    EDS_FILEWRITE('E_RPOLY_CODE_B2',0,15,E_RPOLY_CODE_B2)
    EDS_FILEWRITE('E_RCAL_CODE_B3',0,15,E_RCAL_CODE_B3)
    EDS_FILEWRITE('E_RPOLY_CODE_B3',0,15,E_RPOLY_CODE_B3)
    EDS_FILEWRITE('E_RCAL_CODE_B4',0,15,E_RCAL_CODE_B4)
    EDS_FILEWRITE('E_RPOLY_CODE_B4',0,15,E_RPOLY_CODE_B4)
    EDS_FILEWRITE('E_RC_CODE',0,8,E_RC_CODE)
    EDS_FILEWRITE('E_XO_CAPTRIM1',0,25,E_XO_CAPTRIM1)
    EDS_FILEWRITE('CAPTRIM_X2',0,2,CAPTRIM_X2)
    EDS_FILEWRITE('E_XO_AMP_PROG',0,9,E_XO_AMP_PROG)
    EDS_FILEWRITE('E_LOCK',0,1,E_LOCK)
    EDS_FILE_CLOSE()
### EXCLUDE THIS FOR ATE ##########################


### STEP_4 END
#######################################################################################################

