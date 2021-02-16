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
        <#assign GEN_APP_RTOS_TASK_SIZE_STR = "HarmonyCore.GEN_APP_RTOS_TASK_" + i + "_SIZE">
        <#assign GEN_APP_RTOS_TASK_SIZE = GEN_APP_RTOS_TASK_SIZE_STR?eval>
        <#assign GEN_APP_RTOS_TASK_PRIO_STR = "HarmonyCore.GEN_APP_RTOS_TASK_" + i + "_PRIO">
        <#assign GEN_APP_RTOS_TASK_PRIO = GEN_APP_RTOS_TASK_PRIO_STR?eval>
        <#if HarmonyCore.SELECT_RTOS == "MbedOS">
        <#lt>    /* Create the _${GEN_APP_TASK_NAME?upper_case}_Tasks task */
        <#lt>    Thread ${GEN_APP_TASK_NAME?lower_case}_thread((osPriority)(osPriorityNormal + (${GEN_APP_RTOS_TASK_PRIO} - 1)), ${GEN_APP_RTOS_TASK_SIZE}, NULL, "_${GEN_APP_TASK_NAME?upper_case}_Tasks");
        <#lt>    ${GEN_APP_TASK_NAME?lower_case}_thread.start(callback(_${GEN_APP_TASK_NAME?upper_case}_Tasks, (void *)0));

        </#if>
    </#list>
</#if>