<#--
/*******************************************************************************
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
*******************************************************************************/
-->
<#if HarmonyCore?? >
    <#list 0..(HarmonyCore.GEN_APP_TASK_COUNT - 1) as i>
        <#assign GEN_APP_TASK_NAME_STR = "HarmonyCore.GEN_APP_TASK_NAME_" + i>
        <#assign GEN_APP_TASK_NAME = GEN_APP_TASK_NAME_STR?eval>
        <#assign GEN_APP_RTOS_TASK_USE_DELAY_STR = "HarmonyCore.GEN_APP_RTOS_TASK_" + i + "_USE_DELAY">
        <#assign GEN_APP_RTOS_TASK_USE_DELAY = GEN_APP_RTOS_TASK_USE_DELAY_STR?eval>
        <#assign GEN_APP_RTOS_TASK_DELAY_STR = "HarmonyCore.GEN_APP_RTOS_TASK_" + i + "_DELAY">
        <#assign GEN_APP_RTOS_TASK_DELAY = GEN_APP_RTOS_TASK_DELAY_STR?eval>
        <#if HarmonyCore.SELECT_RTOS == "MbedOS">
            <#lt>static void _${GEN_APP_TASK_NAME?upper_case}_Tasks(void *parameters)
            <#lt>{
            <#lt>    while(1)
            <#lt>    {
            <#lt>        ${GEN_APP_TASK_NAME?upper_case}_Tasks();
            <#if GEN_APP_RTOS_TASK_USE_DELAY == true>
                <#lt>        thread_sleep_for((uint32_t)(${GEN_APP_RTOS_TASK_DELAY} / (MBED_OS_TICK_PERIOD_MS)));
            </#if>
            <#lt>    }
            <#lt>}

        </#if>
    </#list>
</#if>
