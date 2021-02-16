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
###############################################################################
########################## Mbed OS RTOS Configurations ########################
###############################################################################
import os
global coreArch

exclusionList = ["platform.h", "mbed_board.c", "mbed_rtc_time.cpp", "except.S", "irq_cm0.S", "mbed_rtos_rtx.c", "mbed.h", "mbed_boot_gcc_arm.c", "mbed_boot.c", "static_pinmap.h", "mbed_retarget.cpp"]

def AddMbedOSFiles(component, dirPath, destPath, projectPath):
    dirPath = str(Module.getPath() + dirPath)
    fileNames = os.listdir(dirPath)
    for fileName in fileNames:
        # Find mbedos source/header/assembler files
        if fileName.endswith(('.c', '.cpp', '.s', '.S', '.h')):
            # Dont process files in the exclusion list
            if fileName in exclusionList:
                continue
            # Get the relative path of the file w.r.t to the module path
            sourcePath = os.path.relpath(os.path.join(dirPath, fileName), Module.getPath())
            #create a file symbol
            fileSymbolName =  "MBED_OS_" + fileName.replace(".", "_").upper()
            mbedosFile = component.createFileSymbol(fileSymbolName, None)
            mbedosFile.setSourcePath(sourcePath)
            mbedosFile.setDestPath(destPath)
            mbedosFile.setProjectPath(projectPath)
            mbedosFile.setMarkup(False)
            # if it is a source
            if fileName.endswith(('.c', '.cpp', '.s', '.S')):
                mbedosFile.setType("SOURCE")
            else:
                mbedosFile.setType("HEADER")
            mbedosFile.setDependencies(lambda symbol, event: symbol.setEnabled(Database.getSymbolValue("core", "COMPILER_CHOICE") == 0), ['core.COMPILER_CHOICE'])
            mbedosFile.setEnabled(Database.getSymbolValue("core", "COMPILER_CHOICE")  == 0)

def AddMbedOSTemplateFiles(component, dirPath, destPath, projectPath):
    dirPath = str(Module.getPath() + dirPath)
    fileNames = os.listdir(dirPath)
    templateExclusionList = ["None"]
    for fileName in fileNames:
        # Find mbedos source/header/assembler files
        if fileName.endswith(('.c', '.cpp', '.s', '.S', '.h', '.md', '.git', '.json')) == False:
            # Dont process files in the exclusion list
            if fileName in templateExclusionList:
                continue
            # Get the relative path of the file w.r.t to the module path
            sourcePath = os.path.relpath(os.path.join(dirPath, fileName), Module.getPath())
            #create a file symbol
            fileSymbolName =  "MBED_OS_" + fileName.upper()
            mbedosFile = component.createFileSymbol(fileSymbolName, None)
            mbedosFile.setSourcePath(sourcePath)
            mbedosFile.setDestPath(destPath)
            mbedosFile.setProjectPath(projectPath)
            mbedosFile.setMarkup(False)
            mbedosFile.setType("HEADER")

def AddMbedOSSingleFile(component, dirPath, fileName, destPath, projectPath):
    dirPath = str(Module.getPath() + dirPath)
    # Find mbedos source/header/assembler files
    if fileName.endswith(('.c', '.cpp', '.s', '.S', '.h')):
        # Get the relative path of the file w.r.t to the module path
        sourcePath = os.path.relpath(os.path.join(dirPath, fileName), Module.getPath())
        #create a file symbol
        fileSymbolName =  "MBED_OS_" + fileName.replace(".", "_").upper()
        mbedosFile = component.createFileSymbol(fileSymbolName, None)
        mbedosFile.setSourcePath(sourcePath)
        mbedosFile.setDestPath(destPath)
        mbedosFile.setProjectPath(projectPath)
        mbedosFile.setMarkup(False)
        # if it is a source
        if fileName.endswith(('.c', '.cpp', '.s', '.S')):
            mbedosFile.setType("SOURCE")
        else:
            mbedosFile.setType("HEADER")
        mbedosFile.setDependencies(lambda symbol, event: symbol.setEnabled(Database.getSymbolValue("core", "COMPILER_CHOICE") == 0), ['core.COMPILER_CHOICE'])
        mbedosFile.setEnabled(Database.getSymbolValue("core", "COMPILER_CHOICE")  == 0)

def deactivateActiveRtos():
    activeComponents = Database.getActiveComponentIDs()

    for i in range(0, len(activeComponents)):
        if (activeComponents[i] == "FreeRTOS"):
            res = Database.deactivateComponents(["FreeRTOS"])
        elif (activeComponents[i] == "MicriumOSIII"):
            res = Database.deactivateComponents(["MicriumOSIII"])
        elif (activeComponents[i] == "ThreadX"):
            res = Database.deactivateComponents(["ThreadX"])

def mbedosInterruptConfig():
    SysTickInterruptEnable      = "SysTick_INTERRUPT_ENABLE"
    SysTickInterruptHandler     = "SysTick_INTERRUPT_HANDLER"
    SysTickInterruptHandlerLock = "SysTick_INTERRUPT_HANDLER_LOCK"

    if (Database.getSymbolValue("core", SysTickInterruptEnable) == False):
        Database.sendMessage("core", SysTickInterruptEnable, {"isEnabled":True})

    if (Database.getSymbolValue("core", SysTickInterruptHandler) != "SysTick_Handler"):
        Database.sendMessage("core", SysTickInterruptHandler, {"intHandler":"SysTick_Handler"})

    if (Database.getSymbolValue("core", SysTickInterruptHandlerLock) == False):
        Database.sendMessage("core", SysTickInterruptHandlerLock, {"isEnabled":True})

    PendSVInterruptEnable       = "PendSV_INTERRUPT_ENABLE"
    PendSVInterruptHandler      = "PendSV_INTERRUPT_HANDLER"
    PendSVInterruptHandlerLock  = "PendSV_INTERRUPT_HANDLER_LOCK"

    if (Database.getSymbolValue("core", PendSVInterruptEnable) == False):
        Database.sendMessage("core", PendSVInterruptEnable, {"isEnabled":True})

    if (Database.getSymbolValue("core", PendSVInterruptHandler) != "PendSV_Handler"):
        Database.sendMessage("core", PendSVInterruptHandler, {"intHandler":"PendSV_Handler"})

    if (Database.getSymbolValue("core", PendSVInterruptHandlerLock) == False):
        Database.sendMessage("core", PendSVInterruptHandlerLock, {"isEnabled":True})

    SVCallInterruptEnable       = "SVCall_INTERRUPT_ENABLE"
    SVCallInterruptHandler      = "SVCall_INTERRUPT_HANDLER"
    SVCallInterruptHandlerLock  = "SVCall_INTERRUPT_HANDLER_LOCK"

    if (Database.getSymbolValue("core", SVCallInterruptEnable) == False):
        Database.sendMessage("core", SVCallInterruptEnable, {"isEnabled":True})

    if (Database.getSymbolValue("core", SVCallInterruptHandler) != "SVC_Handler"):
        Database.sendMessage("core", SVCallInterruptHandler, {"intHandler":"SVC_Handler"})

    if (Database.getSymbolValue("core", SVCallInterruptHandlerLock) == False):
        Database.sendMessage("core", SVCallInterruptHandlerLock, {"isEnabled":True})

def mbedosCpuClockHz(symbol, event):
    clock = int(event["value"])
    symbol.setValue(clock)

def mbedosCalcTickRate(symbol, event):
    if (event["value"] != 0):
        symbol.setValue(long((1000 / event["value"])))
    else:
        symbol.setValue(0)

def mbedosCheckTickRate(symbol, event):
    symbol.setVisible(False)
    if (event["value"] == 0):
        symbol.setVisible(True)

def destroyComponent(thirdPartyMbedOS):
    Database.sendMessage("core", "SysTick_INTERRUPT_ENABLE", {"isEnabled":False})
    Database.sendMessage("core", "SysTick_INTERRUPT_HANDLER", {"intHandler":"SysTick_Handler"})
    Database.sendMessage("core", "SysTick_INTERRUPT_HANDLER_LOCK", {"isEnabled":False})
    Database.sendMessage("core", "PendSV_INTERRUPT_HANDLER", {"intHandler":"PendSV_Handler"})
    Database.sendMessage("core", "SVCall_INTERRUPT_HANDLER", {"intHandler":"SVCall_Handler"})

# Instatntiate MbedOS Component
def instantiateComponent(thirdPartyMbedOS):
    Log.writeInfoMessage("Running MbedOS RTOS")

    global coreArch

    # Fetch Core Architecture and Family details
    coreArch     = Database.getSymbolValue("core", "CoreArchitecture")
    coreFamily   = ATDF.getNode( "/avr-tools-device-file/devices/device" ).getAttribute( "family" )
    compiler     = Database.getSymbolValue("core", "COMPILER_CHOICE")

    # Deactivate the active RTOS if any.
    deactivateActiveRtos()

    #Mbed OS Interrupt Handlers configurations
    mbedosInterruptConfig()

    #Mbed OS RTOS Configuration Menu
    mbedosSym_CpuClockHz = thirdPartyMbedOS.createIntegerSymbol("MBED_OS_CPU_CLOCK_HZ", None)
    mbedosSym_CpuClockHz.setLabel("CPU Clock Speed (Hz)")
    mbedosSym_CpuClockHz.setDescription("This is the CPU clock speed obtained from the Clock System Service configuration.")
    mbedosSym_CpuClockHz.setReadOnly(True)

    mbedosSym_TickRate = thirdPartyMbedOS.createIntegerSymbol("MBED_OS_TICK_RATE_HZ", None)
    mbedosSym_TickRate.setLabel("Tick Rate (Hz)")
    mbedosSym_TickRate.setDescription("MbedOS - Tick rate (Hz)")
    mbedosSym_TickRate.setDefaultValue(1000)

    mbedosSym_TickRateComment = thirdPartyMbedOS.createCommentSymbol("MBED_OS_TICK_RATE_COMMENT", None)
    mbedosSym_TickRateComment.setLabel("Warning!!! Tick Rate cannot be \"0\" !!!")
    mbedosSym_TickRateComment.setVisible(False)
    mbedosSym_TickRateComment.setDependencies(mbedosCheckTickRate, ["MBED_OS_TICK_RATE_HZ"])

    mbedosSym_RTOSMenu = thirdPartyMbedOS.createMenuSymbol("MBED_OS_RTOS_CONFIGURATION_MENU", None)
    mbedosSym_RTOSMenu.setLabel("RTOS Configuration")
    mbedosSym_RTOSMenu.setDescription("Mbed OS RTOS Configuration Parameters")

    mbedosSym_rtosPresent = thirdPartyMbedOS.createBooleanSymbol("MBED_CONF_RTOS_PRESENT", mbedosSym_RTOSMenu)
    mbedosSym_rtosPresent.setLabel("Mbed OS RTOS present")
    mbedosSym_rtosPresent.setDefaultValue(True)
    mbedosSym_rtosPresent.setReadOnly(True)
    mbedosSym_rtosPresent.setDescription("Mbed OS RTOS Present")

    mbedosSym_rtosIdleThreadStackSize = thirdPartyMbedOS.createIntegerSymbol("MBED_CONF_RTOS_IDLE_THREAD_STACK_SIZE", mbedosSym_RTOSMenu)
    mbedosSym_rtosIdleThreadStackSize.setLabel("RTOS idle thread stack size")
    mbedosSym_rtosIdleThreadStackSize.setDefaultValue(512)
    mbedosSym_rtosIdleThreadStackSize.setDescription("The size of the idle thread's stack")

    mbedosSym_rtosIdleThreadStackSizeDebugExtra = thirdPartyMbedOS.createIntegerSymbol("MBED_CONF_RTOS_IDLE_THREAD_STACK_SIZE_DEBUG_EXTRA", mbedosSym_RTOSMenu)
    mbedosSym_rtosIdleThreadStackSizeDebugExtra.setLabel("RTOS idle thread stack size debug extra")
    mbedosSym_rtosIdleThreadStackSizeDebugExtra.setDefaultValue(128)
    mbedosSym_rtosIdleThreadStackSizeDebugExtra.setDescription("Additional size to add to the idle thread when code compilation optimisation is disabled")

    mbedosSym_rtosIdleThreadStackSizeTicklessExtra = thirdPartyMbedOS.createIntegerSymbol("MBED_CONF_RTOS_IDLE_THREAD_STACK_SIZE_TICKLESS_EXTRA", mbedosSym_RTOSMenu)
    mbedosSym_rtosIdleThreadStackSizeTicklessExtra.setLabel("RTOS idle thread stack size tickless extra")
    mbedosSym_rtosIdleThreadStackSizeTicklessExtra.setDefaultValue(256)
    mbedosSym_rtosIdleThreadStackSizeTicklessExtra.setDescription("Additional size to add to the idle thread when tickless is enabled and LPTICKER_DELAY_TICKS is used")

    mbedosSym_rtosMainThreadStackSize = thirdPartyMbedOS.createIntegerSymbol("MBED_CONF_RTOS_MAIN_THREAD_STACK_SIZE", mbedosSym_RTOSMenu)
    mbedosSym_rtosMainThreadStackSize.setLabel("RTOS main thread stack size")
    mbedosSym_rtosMainThreadStackSize.setDefaultValue(1024)
    mbedosSym_rtosMainThreadStackSize.setDescription("The size of the main thread's stack")

    mbedosSym_rtosThreadStackSize = thirdPartyMbedOS.createIntegerSymbol("MBED_CONF_RTOS_THREAD_STACK_SIZE", mbedosSym_RTOSMenu)
    mbedosSym_rtosThreadStackSize.setLabel("RTOS thread stack size")
    mbedosSym_rtosThreadStackSize.setDefaultValue(512)
    mbedosSym_rtosThreadStackSize.setDescription("The default stack size of new threads")

    mbedosSym_rtosTimerThreadStackSize = thirdPartyMbedOS.createIntegerSymbol("MBED_CONF_RTOS_TIMER_THREAD_STACK_SIZE", mbedosSym_RTOSMenu)
    mbedosSym_rtosTimerThreadStackSize.setLabel("RTOS timer thread stack size")
    mbedosSym_rtosTimerThreadStackSize.setDefaultValue(768)
    mbedosSym_rtosTimerThreadStackSize.setDescription("The size of the timer thread's stack")

    # MbedOS Generic Source Files
    configName = Variables.get("__CONFIGURATION_NAME")

    mbedosConfigFile = thirdPartyMbedOS.createFileSymbol("MBED_OS_MBED_CONFIG_H", None)
    mbedosConfigFile.setSourcePath("templates/mbed_os/mbed_config.h.ftl")
    mbedosConfigFile.setOutputName("mbed_config.h")
    mbedosConfigFile.setDestPath("mbedos_config/")
    mbedosConfigFile.setProjectPath("config/" + configName + "/mbedos_config/")
    mbedosConfigFile.setType("HEADER")
    mbedosConfigFile.setMarkup(True)

    mbedosRtxFile = thirdPartyMbedOS.createFileSymbol("MBED_OS_MBED_RTX_H", None)
    mbedosRtxFile.setSourcePath("templates/mbed_os/mbed_rtx.h.ftl")
    mbedosRtxFile.setOutputName("mbed_rtx.h")
    mbedosRtxFile.setDestPath("mbedos_config/")
    mbedosRtxFile.setProjectPath("config/" + configName + "/mbedos_config/")
    mbedosRtxFile.setType("HEADER")
    mbedosRtxFile.setMarkup(True)

    mbedosCmsisFile = thirdPartyMbedOS.createFileSymbol("MBED_OS_MBED_CMSIS_H", None)
    mbedosCmsisFile.setSourcePath("templates/mbed_os/cmsis.h")
    mbedosCmsisFile.setOutputName("cmsis.h")
    mbedosCmsisFile.setDestPath("../../third_party/rtos/mbed-os/targets/")
    mbedosCmsisFile.setProjectPath("mbed-os/targets")
    mbedosCmsisFile.setType("HEADER")
    mbedosCmsisFile.setMarkup(False)

    mbedosSystemDefFile = thirdPartyMbedOS.createFileSymbol("MBED_OS_SYS_DEF", None)
    mbedosSystemDefFile.setType("STRING")
    mbedosSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    mbedosSystemDefFile.setSourcePath("templates/system/definitions.h.ftl")
    mbedosSystemDefFile.setMarkup(True)

    mbedosSystemTasksFile = thirdPartyMbedOS.createFileSymbol("MBED_OS_SYS_START_SCHED", None)
    mbedosSystemTasksFile.setType("STRING")
    mbedosSystemTasksFile.setOutputName("core.LIST_SYSTEM_RTOS_TASKS_C_CALL_SCHEDULAR")
    mbedosSystemTasksFile.setSourcePath("templates/system/start_rtos.c.ftl")
    mbedosSystemTasksFile.setMarkup(True)

    mbedosSystemTasksCpp = thirdPartyMbedOS.createFileSymbol("MBED_OS_SYS_TASKS", None)
    mbedosSystemTasksCpp.setType("STRING")
    mbedosSystemTasksCpp.setOutputName("core.LIST_SYSTEM_RTOS_TASKS_C_GEN_APP")
    mbedosSystemTasksCpp.setSourcePath("templates/system/create_tasks.cpp.ftl")
    mbedosSystemTasksCpp.setMarkup(True)

    mbedosSystemTasksDef = thirdPartyMbedOS.createFileSymbol("MBED_OS_SYS_TASKS_DEF", None)
    mbedosSystemTasksDef.setType("STRING")
    mbedosSystemTasksDef.setOutputName("core.LIST_SYSTEM_RTOS_TASKS_C_DEFINITIONS")
    mbedosSystemTasksDef.setSourcePath("templates/system/tasks_macros.cpp.ftl")
    mbedosSystemTasksDef.setMarkup(True)

    mbedosSystemInitDef = thirdPartyMbedOS.createFileSymbol("MBED_OS_INIT_DEF", None)
    mbedosSystemInitDef.setType("STRING")
    mbedosSystemInitDef.setOutputName("core.LIST_SYSTEM_INIT_C_SYSTEM_INITIALIZATION")
    mbedosSystemInitDef.setSourcePath("templates/system/initialization_definitions.c.ftl")
    mbedosSystemInitDef.setMarkup(True)

    coreName = coreArch.replace("-", "_").replace("PLUS", "").lower()

    # Mbed OS RTOS
    AddMbedOSFiles(thirdPartyMbedOS, "../mbed-os/", "../../third_party/rtos/mbed-os", "mbed-os")
    AddMbedOSFiles(thirdPartyMbedOS, "../mbed-os/rtos/source/", "../../third_party/rtos/mbed-os/rtos/source", "mbed-os/rtos/source")
    AddMbedOSFiles(thirdPartyMbedOS, "../mbed-os/rtos/include/rtos/", "../../third_party/rtos/mbed-os/rtos/include/rtos", "mbed-os/rtos/include/rtos")
    AddMbedOSFiles(thirdPartyMbedOS, "../mbed-os/rtos/include/rtos/internal/", "../../third_party/rtos/mbed-os/rtos/include/rtos/internal", "mbed-os/rtos/include/rtos/internal")
    AddMbedOSSingleFile(thirdPartyMbedOS, "templates/mbed_os/", "mbed_rtos_rtx.c", "../../third_party/rtos/mbed-os/cmsis/device/rtos/source", "mbed-os/cmsis/device/rtos/source")
    AddMbedOSSingleFile(thirdPartyMbedOS, "templates/mbed_os/", "mbed.h", "../../third_party/rtos/mbed-os", "mbed-os")

    # Mbed OS CMSIS RTOS2
    AddMbedOSFiles(thirdPartyMbedOS, "../mbed-os/cmsis/CMSIS_5/CMSIS/RTOS2/Source/", "../../third_party/rtos/mbed-os/cmsis/CMSIS_5/CMSIS/RTOS2/Source", "mbed-os/cmsis/CMSIS_5/CMSIS/RTOS2/Source")
    AddMbedOSFiles(thirdPartyMbedOS, "../mbed-os/cmsis/CMSIS_5/CMSIS/RTOS2/Include/", "../../third_party/rtos/mbed-os/cmsis/CMSIS_5/CMSIS/RTOS2/Include", "mbed-os/cmsis/CMSIS_5/CMSIS/RTOS2/Include")
    AddMbedOSFiles(thirdPartyMbedOS, "../mbed-os/cmsis/CMSIS_5/CMSIS/RTOS2/RTX/Config/", "../../third_party/rtos/mbed-os/cmsis/CMSIS_5/CMSIS/RTOS2/RTX/Config", "mbed-os/cmsis/CMSIS_5/CMSIS/RTOS2/RTX/Config")
    AddMbedOSFiles(thirdPartyMbedOS, "../mbed-os/cmsis/CMSIS_5/CMSIS/RTOS2/RTX/Include/", "../../third_party/rtos/mbed-os/cmsis/CMSIS_5/CMSIS/RTOS2/RTX/Include", "mbed-os/cmsis/CMSIS_5/CMSIS/RTOS2/RTX/Include")
    AddMbedOSFiles(thirdPartyMbedOS, "../mbed-os/cmsis/CMSIS_5/CMSIS/RTOS2/RTX/Include1/", "../../third_party/rtos/mbed-os/cmsis/CMSIS_5/CMSIS/RTOS2/RTX/Include1", "mbed-os/cmsis/CMSIS_5/CMSIS/RTOS2/RTX/Include1")
    AddMbedOSFiles(thirdPartyMbedOS, "../mbed-os/cmsis/CMSIS_5/CMSIS/RTOS2/RTX/Library/", "../../third_party/rtos/mbed-os/cmsis/CMSIS_5/CMSIS/RTOS2/RTX/Library", "mbed-os/cmsis/CMSIS_5/CMSIS/RTOS2/RTX/Library")
    AddMbedOSFiles(thirdPartyMbedOS, "../mbed-os/cmsis/CMSIS_5/CMSIS/RTOS2/RTX/Source/", "../../third_party/rtos/mbed-os/cmsis/CMSIS_5/CMSIS/RTOS2/RTX/Source", "mbed-os/cmsis/CMSIS_5/CMSIS/RTOS2/RTX/Source")
    AddMbedOSFiles(thirdPartyMbedOS, "../mbed-os/cmsis/device/", "../../third_party/rtos/mbed-os/cmsis/device", "mbed-os/cmsis/device")
    AddMbedOSFiles(thirdPartyMbedOS, "../mbed-os/cmsis/device/rtos/include/", "../../third_party/rtos/mbed-os/cmsis/device/rtos/include", "mbed-os/cmsis/device/rtos/include")
    AddMbedOSFiles(thirdPartyMbedOS, "../mbed-os/cmsis/device/rtos/source/", "../../third_party/rtos/mbed-os/cmsis/device/rtos/source", "mbed-os/cmsis/device/rtos/source")
    AddMbedOSFiles(thirdPartyMbedOS, "../mbed-os/cmsis/device/RTE/include/", "../../third_party/rtos/mbed-os/cmsis/device/RTE/include", "mbed-os/cmsis/device/RTE/include")

    # Mbed OS Platform
    AddMbedOSFiles(thirdPartyMbedOS, "../mbed-os/platform/include/platform/", "../../third_party/rtos/mbed-os/platform/include/platform", "mbed-os/platform/include/platform")
    AddMbedOSFiles(thirdPartyMbedOS, "../mbed-os/platform/include/platform/internal/", "../../third_party/rtos/mbed-os/platform/include/platform/internal", "mbed-os/platform/include/platform/internal")
    AddMbedOSFiles(thirdPartyMbedOS, "../mbed-os/platform/cxxsupport/", "../../third_party/rtos/mbed-os/platform/cxxsupport", "mbed-os/platform/cxxsupport")
    AddMbedOSTemplateFiles(thirdPartyMbedOS, "../mbed-os/platform/cxxsupport/", "../../third_party/rtos/mbed-os/platform/cxxsupport", "mbed-os/platform/cxxsupport")
    AddMbedOSSingleFile(thirdPartyMbedOS, "../mbed-os/platform/source/", "mbed_assert.c", "../../third_party/rtos/mbed-os/platform/source", "mbed-os/platform/source")
    AddMbedOSSingleFile(thirdPartyMbedOS, "../mbed-os/platform/source/", "mbed_atomic_impl.c", "../../third_party/rtos/mbed-os/platform/source", "mbed-os/platform/source")
    AddMbedOSSingleFile(thirdPartyMbedOS, "../mbed-os/platform/source/", "mbed_critical.c", "../../third_party/rtos/mbed-os/platform/source", "mbed-os/platform/source")
    AddMbedOSSingleFile(thirdPartyMbedOS, "../mbed-os/platform/source/", "mbed_error.c", "../../third_party/rtos/mbed-os/platform/source", "mbed-os/platform/source")
    AddMbedOSSingleFile(thirdPartyMbedOS, "../mbed-os/platform/source/", "mbed_power_mgmt.c", "../../third_party/rtos/mbed-os/platform/source", "mbed-os/platform/source")
    AddMbedOSSingleFile(thirdPartyMbedOS, "../mbed-os/platform/source/", "mbed_thread.cpp", "../../third_party/rtos/mbed-os/platform/source", "mbed-os/platform/source")
    AddMbedOSSingleFile(thirdPartyMbedOS, "../mbed-os/platform/source/", "mbed_os_timer.cpp", "../../third_party/rtos/mbed-os/platform/source", "mbed-os/platform/source")
    AddMbedOSSingleFile(thirdPartyMbedOS, "templates/mbed_os/", "mbed_board.c", "../../third_party/rtos/mbed-os/platform/source", "mbed-os/platform/source")
    AddMbedOSSingleFile(thirdPartyMbedOS, "../mbed-os/platform/source/", "mbed_crash_data_offsets.h", "../../third_party/rtos/mbed-os/platform/source", "mbed-os/platform/source")
    AddMbedOSSingleFile(thirdPartyMbedOS, "templates/mbed_os/", "platform.h", "../../third_party/rtos/mbed-os/platform", "mbed-os/platform")
    AddMbedOSSingleFile(thirdPartyMbedOS, "../mbed-os/drivers/include/drivers/", "TimerEvent.h", "../../third_party/rtos/mbed-os/drivers/include/drivers", "mbed-os/drivers/include/drivers")
    AddMbedOSSingleFile(thirdPartyMbedOS, "../mbed-os/drivers/include/drivers/", "TickerDataClock.h", "../../third_party/rtos/mbed-os/drivers/include/drivers", "mbed-os/drivers/include/drivers")
    AddMbedOSSingleFile(thirdPartyMbedOS, "../mbed-os/drivers/include/drivers/", "MbedCRC.h", "../../third_party/rtos/mbed-os/drivers/include/drivers", "mbed-os/drivers/include/drivers")
    AddMbedOSSingleFile(thirdPartyMbedOS, "../mbed-os/hal/include/hal/", "ticker_api.h", "../../third_party/rtos/mbed-os/hal/include/hal", "mbed-os/hal/include/hal")
    AddMbedOSSingleFile(thirdPartyMbedOS, "../mbed-os/hal/include/hal/", "us_ticker_api.h", "../../third_party/rtos/mbed-os/hal/include/hal", "mbed-os/hal/include/hal")
    AddMbedOSSingleFile(thirdPartyMbedOS, "../mbed-os/hal/include/hal/", "lp_ticker_api.h", "../../third_party/rtos/mbed-os/hal/include/hal", "mbed-os/hal/include/hal")
    AddMbedOSSingleFile(thirdPartyMbedOS, "../mbed-os/hal/include/hal/", "critical_section_api.h", "../../third_party/rtos/mbed-os/hal/include/hal", "mbed-os/hal/include/hal")
    AddMbedOSSingleFile(thirdPartyMbedOS, "../mbed-os/hal/include/hal/", "crc_api.h", "../../third_party/rtos/mbed-os/hal/include/hal", "mbed-os/hal/include/hal")
    AddMbedOSSingleFile(thirdPartyMbedOS, "../mbed-os/hal/source/", "mbed_critical_section_api.c", "../../third_party/rtos/mbed-os/hal/source", "mbed-os/hal/source")
    AddMbedOSSingleFile(thirdPartyMbedOS, "../mbed-os/hal/include/hal/", "sleep_api.h", "../../third_party/rtos/mbed-os/hal/include/hal", "mbed-os/hal/include/hal")

    execfile(Module.getPath() + "config/arch/arm/devices_" + coreName + "/mbedos_config.py")
