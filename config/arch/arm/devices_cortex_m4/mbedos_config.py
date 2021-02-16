# coding: utf-8
"""*****************************************************************************
* Copyright (C) 2020 Microchip Technology Inc. and its subsidiaries.
*
* Subject to your compliance with these terms, you may use Microchip software
* and any derivatives exclusively with Microchip products. It is your
* responsibility to comply with third party license terms applicable to your
* use of third party software (including open source software) that may
* accompany Microchip software.
*
* THIS SOFTWARE IS SUPPLIED BY MICROCHIP "AS IS". NO WARRANTIES, WHETHER
* EXPRESS, IMPLIED OR STATUTORY, APPLY TO THIS SOFTWARE, INCLUDING ANY IMPLIED
* WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A
* PARTICULAR PURPOSE.
*
* IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT, SPECIAL, PUNITIVE,
* INCIDENTAL OR CONSEQUENTIAL LOSS, DAMAGE, COST OR EXPENSE OF ANY KIND
* WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAUSED, EVEN IF MICROCHIP HAS
* BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE FORESEEABLE. TO THE
* FULLEST EXTENT ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL CLAIMS IN
* ANY WAY RELATED TO THIS SOFTWARE WILL NOT EXCEED THE AMOUNT OF FEES, IF ANY,
* THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THIS SOFTWARE.
*****************************************************************************"""

############################################################################
############### Cortex-M4 Architecture specific configuration ##############
############################################################################
#CPU Clock Frequency
mbedosSym_CpuClockHz.setDependencies(mbedosCpuClockHz, ["core.CPU_CLOCK_FREQUENCY"])
mbedosSym_CpuClockHz.setDefaultValue(int(Database.getSymbolValue("core", "CPU_CLOCK_FREQUENCY")))

#Set HEAP size to 20480
dummyDict = {}
dummyDict = Database.sendMessage("core", "HEAP_SIZE", {"heap_size" : 20480})

#Setup SysTick, PendSV and SVCall Interrupt Priorities.
#SysTick must be highest priority
SysTickInterruptHandlerIndex    = Interrupt.getInterruptIndex("SysTick")

SysTickInterruptPri             = "NVIC_"+ str(SysTickInterruptHandlerIndex) +"_0_PRIORITY"
SysTickInterruptPriLock         = "NVIC_"+ str(SysTickInterruptHandlerIndex) +"_0_PRIORITY_LOCK"

if (Database.getSymbolValue("core", SysTickInterruptPri) != "1"):
    Database.clearSymbolValue("core", SysTickInterruptPri)
    Database.setSymbolValue("core", SysTickInterruptPri, "1")

if (Database.getSymbolValue("core", SysTickInterruptPriLock) == False):
    Database.clearSymbolValue("core", SysTickInterruptPriLock)
    Database.setSymbolValue("core", SysTickInterruptPriLock, True)

#SVCall must be lowest priority
SVCallInterruptHandlerIndex    = Interrupt.getInterruptIndex("SVCall")

SVCallInterruptPri             = "NVIC_"+ str(SVCallInterruptHandlerIndex) +"_0_PRIORITY"
SVCallInterruptPriLock         = "NVIC_"+ str(SVCallInterruptHandlerIndex) +"_0_PRIORITY_LOCK"

if (Database.getSymbolValue("core", SVCallInterruptPri) != "7"):
    Database.clearSymbolValue("core", SVCallInterruptPri)
    Database.setSymbolValue("core", SVCallInterruptPri, "7")

if (Database.getSymbolValue("core", SVCallInterruptPriLock) == False):
    Database.clearSymbolValue("core", SVCallInterruptPriLock)
    Database.setSymbolValue("core", SVCallInterruptPriLock, True)

#PndSV must be lowest priority
PendSVInterruptHandlerIndex    = Interrupt.getInterruptIndex("PendSV")

PendSVInterruptPri          = "NVIC_"+ str(PendSVInterruptHandlerIndex) +"_0_PRIORITY"
PendSVInterruptPriLock      = "NVIC_"+ str(PendSVInterruptHandlerIndex) +"_0_PRIORITY_LOCK"

if (Database.getSymbolValue("core", PendSVInterruptPri) != "7"):
    Database.clearSymbolValue("core", PendSVInterruptPri)
    Database.setSymbolValue("core", PendSVInterruptPri, "7")

if (Database.getSymbolValue("core", PendSVInterruptPriLock) == False):
    Database.clearSymbolValue("core", PendSVInterruptPriLock)
    Database.setSymbolValue("core", PendSVInterruptPriLock, True)

# Update C32 Include directories path
mbedosxc32PreprocessroMacroSym = thirdPartyMbedOS.createSettingSymbol("MBED_OS_XC32_PREPROC_MARCOS", None)
mbedosxc32PreprocessroMacroSym.setCategory("C32")
mbedosxc32PreprocessroMacroSym.setKey("preprocessor-macros")
mbedosxc32PreprocessroMacroSym.setValue("__CORTEX_M4;TARGET_M4;TARGET_CORTEX_M;TARGET_LIKE_MBED;__MBED__=1")

mbedosxc32cppPreprocessroMacroSym = thirdPartyMbedOS.createSettingSymbol("MBED_OS_XC32CPP_PREPROC_MARCOS", None)
mbedosxc32cppPreprocessroMacroSym.setCategory("C32CPP")
mbedosxc32cppPreprocessroMacroSym.setKey("preprocessor-macros")
mbedosxc32cppPreprocessroMacroSym.setValue("__CORTEX_M4;TARGET_M4;TARGET_CORTEX_M;TARGET_LIKE_MBED;__MBED__=1")

mbedosxc32asPreprocessroMacroSym = thirdPartyMbedOS.createSettingSymbol("MBED_OS_XC32AS_PREPROC_MARCOS", None)
mbedosxc32asPreprocessroMacroSym.setCategory("C32-AS")
mbedosxc32asPreprocessroMacroSym.setKey("preprocessor-macros")
mbedosxc32asPreprocessroMacroSym.setValue("__CORTEX_M4;TARGET_M4;TARGET_CORTEX_M;TARGET_LIKE_MBED;__MBED__=1")

mbedosOsXc32IncludeSettingSym = thirdPartyMbedOS.createSettingSymbol("MBED_OS_XC32_SETTING_INCLUDE_HEADER", None)
mbedosOsXc32IncludeSettingSym.setCategory("C32")
mbedosOsXc32IncludeSettingSym.setKey("appendMe")
mbedosOsXc32IncludeSettingSym.setValue("-include ../src/config/" + configName + "/mbedos_config/mbed_config.h")
mbedosOsXc32IncludeSettingSym.setAppend(True, " ")

mbedosOsXc32cppIncludeSettingSym = thirdPartyMbedOS.createSettingSymbol("MBED_OS_XC32CPP_SETTING_INCLUDE_HEADER", None)
mbedosOsXc32cppIncludeSettingSym.setCategory("C32CPP")
mbedosOsXc32cppIncludeSettingSym.setKey("appendMe")
mbedosOsXc32cppIncludeSettingSym.setValue("-include ../src/config/" + configName + "/mbedos_config/mbed_config.h")
mbedosOsXc32cppIncludeSettingSym.setAppend(True, " ")

mbedosOsXc32asIncludeSettingSym = thirdPartyMbedOS.createSettingSymbol("MBED_OS_XC32AS_SETTING_INCLUDE_HEADER", None)
mbedosOsXc32asIncludeSettingSym.setCategory("C32-AS")
mbedosOsXc32asIncludeSettingSym.setKey("appendMe")
mbedosOsXc32asIncludeSettingSym.setValue("-include ../src/config/" + configName + "/mbedos_config/mbed_config.h")
mbedosOsXc32asIncludeSettingSym.setAppend(True, " ")

mbedosIncludePath = "../src/config/" + configName + "/mbedos_config;../src/third_party/rtos/mbed-os;\
../src/third_party/rtos/mbed-os/rtos/source;../src/third_party/rtos/mbed-os/rtos/include;../src/third_party/rtos/mbed-os/rtos/include/rtos;../src/third_party/rtos/mbed-os/rtos/include/rtos/internal;\
../src/third_party/rtos/mbed-os/events/include;../src/third_party/rtos/mbed-os/events/include/events;../src/third_party/rtos/mbed-os/events/include/events/internal;\
../src/third_party/rtos/mbed-os/platform;../src/third_party/rtos/mbed-os/platform/include;../src/third_party/rtos/mbed-os/platform/include/platform;../src/third_party/rtos/mbed-os/platform/include/platform/internal;\
../src/third_party/rtos/mbed-os/platform/cxxsupport;../src/third_party/rtos/mbed-os/platform/source;\
../src/third_party/rtos/mbed-os/cmsis/CMSIS_5/CMSIS/RTOS2/Include;\
../src/third_party/rtos/mbed-os/cmsis/CMSIS_5/CMSIS/RTOS2/RTX/Config;../src/third_party/rtos/mbed-os/cmsis/CMSIS_5/CMSIS/RTOS2/RTX/Include;\
../src/third_party/rtos/mbed-os/cmsis/CMSIS_5/CMSIS/RTOS2/RTX/Include1;../src/third_party/rtos/mbed-os/cmsis/CMSIS_5/CMSIS/RTOS2/RTX/Source;\
../src/third_party/rtos/mbed-os/cmsis/device;../src/third_party/rtos/mbed-os/cmsis/device/RTE/include;../src/third_party/rtos/mbed-os/cmsis/device/rtos/include;\
../src/third_party/rtos/mbed-os/targets;../src/third_party/rtos/mbed-os/drivers/include/drivers;../src/third_party/rtos/mbed-os/drivers/include;\
../src/third_party/rtos/mbed-os/hal/include/hal;../src/third_party/rtos/mbed-os/hal/include;"

AddMbedOSSingleFile(thirdPartyMbedOS, "templates/mbed_os/TARGET_RTOS_M4_M7/", "irq_cm4f.S", "../../third_party/rtos/mbed-os/cmsis/CMSIS_5/CMSIS/RTOS2/RTX/Source/TOOLCHAIN_GCC/TARGET_RTOS_M4_M7", "mbed-os/cmsis/CMSIS_5/CMSIS/RTOS2/RTX/Source/TOOLCHAIN_GCC/TARGET_RTOS_M4_M7")

mbedosOsXc32SettingSym = thirdPartyMbedOS.createSettingSymbol("MBED_OS_XC32_INCLUDE_DIRS", None)
mbedosOsXc32SettingSym.setCategory("C32")
mbedosOsXc32SettingSym.setKey("extra-include-directories")
mbedosOsXc32SettingSym.setValue(mbedosIncludePath)
mbedosOsXc32SettingSym.setAppend(True, ";")

mbedosOsXc32cppSettingSym = thirdPartyMbedOS.createSettingSymbol("MBED_OS_XC32CPP_INCLUDE_DIRS", None)
mbedosOsXc32cppSettingSym.setCategory("C32CPP")
mbedosOsXc32cppSettingSym.setKey("extra-include-directories")
mbedosOsXc32cppSettingSym.setValue(mbedosIncludePath)
mbedosOsXc32cppSettingSym.setAppend(True, ";")

mbedosIncDirForAsm = thirdPartyMbedOS.createSettingSymbol("MBED_OS_XC32_AS_INCLUDE_DIRS", None)
mbedosIncDirForAsm.setCategory("C32-AS")
mbedosIncDirForAsm.setKey("extra-include-directories-for-assembler")
mbedosIncDirForAsm.setValue(mbedosIncludePath)
mbedosIncDirForAsm.setAppend(True, ";")

mbedosIncDirForPre = thirdPartyMbedOS.createSettingSymbol("MBED_OS_XC32_AS_INCLUDE_PRE_PROC_DIRS", None)
mbedosIncDirForPre.setCategory("C32-AS")
mbedosIncDirForPre.setKey("extra-include-directories-for-preprocessor")
mbedosIncDirForPre.setValue(mbedosIncludePath)
mbedosIncDirForPre.setAppend(True, ";")
