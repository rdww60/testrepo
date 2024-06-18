Attribute VB_Name = "SMB_device_Configuration"
Option Explicit

Sub AU5448_SMB_100KHZ()
    ''***********************************************************************************************************
    ''                                   AU5448 SMB 100KHZ
    ''***********************************************************************************************************
    ''*** Location of Python scripts to be converted for AU5411 devices
    ''*** Location of the converter files for AU5411 devices
    ''***********************************************************************************************************
    strPyPatternFilesPath = "E:\Aura\PY_PATTERNS\EXAMPLES\AU5448_EXAMPLE\"
    strPyPatternFilesPath = "E:\Aura\AU5448\Program\AU5448_REV00_RC00\Patterns\TD3\PY_PATTERNS"
    strConverterFilesPath = "E:\Aura\PY_CONVERTER\CONVERTER_FILES\AU5448_CONVERTER_FILES_SMB100KHZ\"
    strSDAPinName = "SMBDAT"
    SDAIO_Column = 75
    Addr_Data_Start = 6
End Sub

Sub AU5448_SMB_400KHZ(TimingMode As String)
    ''***********************************************************************************************************
    ''                                   AU5448 SMB 400KHZ
    ''***********************************************************************************************************
    ''*** Location of Python scripts to be converted for AU5411 devices
    ''*** Location of the converter files for AU5411 devices
    ''***********************************************************************************************************
    strPyPatternFilesPath = "E:\Aura\PY_PATTERNS\EXAMPLES\AU5448_EXAMPLE\"
    strPyPatternFilesPath = "E:\Aura\AU5448\Program\AU5448_REV00_RC00\Patterns\TD3\PY_PATTERNS"
    'strPyPatternFilesPath = "E:\Aura\AU5448\Program\AU5448_REV00_RC00\Patterns\TD3\PY_PATTERNS\20221114_Au5448_ATE_FT_Vectors_Delivery\EFUSE_DEFECTS_SCREEN"
    strPyPatternFilesPath = "E:\Aura\AU5448\Program\AU5448_REV00_RC00\Patterns\TD3\PY_PATTERNS\20221208_Au5448_ATE_FT_Vectors_Delivery"
    strPyPatternFilesPath = "E:\Aura\AU544X\Program\AU544X_REV00_RC00\Patterns\PY_PATTERNS\20230103_Au5448_ATE_FT_Vectors_Delivery"
    'strPyPatternFilesPath = "E:\Aura\AU544X\Program\AU544X_REV00_RC00\Patterns\PY_PATTERNS\20230103_Au5444_ATE_FT_Vectors_Delivery"
    If InStr(1, TimingMode, "SINGLE", vbTextCompare) = 1 Then
        strConverterFilesPath = "E:\Aura\PY_CONVERTER\CONVERTER_FILES\AU5448_CONVERTER_FILES_SMB400KHZ_SINGLE_MODE\"
        Addr_Data_Start = 6
        Vector_Repeat = 3
        Timing_Mode = "single"
    End If
    If InStr(1, TimingMode, "QUAD", vbTextCompare) = 1 Then
        'strConverterFilesPath = "E:\Aura\PY_CONVERTER\CONVERTER_FILES\AU5448_CONVERTER_FILES_SMB400KHZ_QUAD_MODE\"
        strConverterFilesPath = "E:\Aura\PY_CONVERTER\CONVERTER_FILES\AU5448_CONVERTER_FILES_SMB400KHZ_QUAD_MODE_2X\"
        Addr_Data_Start = 18
        Vector_Repeat = 15
        Timing_Mode = "quad"
    End If
    strSDAPinName = "SMBDAT"
    'SDAIO_Column = 75
    SDAIO_Column = 73
    'Addr_Data_Start = 6
    Block_Data_Start = 2
End Sub

