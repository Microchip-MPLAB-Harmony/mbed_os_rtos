/*
 * mbed SDK
 * Copyright (c) 2017 ARM Limited
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#ifndef __MBED_CONFIG_DATA__
#define __MBED_CONFIG_DATA__

// Configuration parameters
#define MBED_CONF_RTOS_API_PRESENT                                            1                                                                                                // set by library:rtos-api
#define MBED_CONF_RTOS_EVFLAGS_NUM                                            0                                                                                                // set by library:rtos
#define MBED_CONF_RTOS_IDLE_THREAD_STACK_SIZE                                 ${MBED_CONF_RTOS_IDLE_THREAD_STACK_SIZE}                                                                                              // set by library:rtos
#define MBED_CONF_RTOS_IDLE_THREAD_STACK_SIZE_DEBUG_EXTRA                     ${MBED_CONF_RTOS_IDLE_THREAD_STACK_SIZE_DEBUG_EXTRA}                                                                                                // set by library:rtos
#define MBED_CONF_RTOS_IDLE_THREAD_STACK_SIZE_TICKLESS_EXTRA                  ${MBED_CONF_RTOS_IDLE_THREAD_STACK_SIZE_TICKLESS_EXTRA}                                                                                              // set by library:rtos
#define MBED_CONF_RTOS_MAIN_THREAD_STACK_SIZE                                 ${MBED_CONF_RTOS_MAIN_THREAD_STACK_SIZE}                                                                                             // set by library:rtos
#define MBED_CONF_RTOS_MSGQUEUE_DATA_SIZE                                     0                                                                                                // set by library:rtos
#define MBED_CONF_RTOS_MSGQUEUE_NUM                                           0                                                                                                // set by library:rtos
#define MBED_CONF_RTOS_MUTEX_NUM                                              0                                                                                                // set by library:rtos
#define MBED_CONF_RTOS_PRESENT                                                1                                                                                                // set by library:rtos
#define MBED_CONF_RTOS_SEMAPHORE_NUM                                          0                                                                                                // set by library:rtos
#define MBED_CONF_RTOS_THREAD_NUM                                             0                                                                                                // set by library:rtos
#define MBED_CONF_RTOS_THREAD_STACK_SIZE                                      ${MBED_CONF_RTOS_THREAD_STACK_SIZE}                                                                                             // set by library:rtos
#define MBED_CONF_RTOS_THREAD_USER_STACK_SIZE                                 0                                                                                                // set by library:rtos
#define MBED_CONF_RTOS_TIMER_NUM                                              0                                                                                                // set by library:rtos
#define MBED_CONF_RTOS_TIMER_THREAD_STACK_SIZE                                ${MBED_CONF_RTOS_TIMER_THREAD_STACK_SIZE}                                                                                              // set by library:rtos
#define MEM_ALLOC                                                             malloc                                                                                           // set by library:mbed-trace
#define MEM_FREE                                                              free                                                                                             // set by library:mbed-trace
#define MBED_CONF_PLATFORM_STDIO_MINIMAL_CONSOLE_ONLY                         1
#define _RTE_                                                                                                                                                                  // defined by library:rtos

<#if core.COMPILER_CHOICE == "XC32">
#ifndef __LANGUAGE_ASSEMBLY__
<#elseif core.COMPILER_CHOICE == "IAR">
#ifdef __ICCARM__
</#if>
#include <stdint.h>
extern uint32_t SystemCoreClock;
// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility
extern "C" {
#endif
// DOM-IGNORE-END
void mbed_rtos_init();
void mbed_rtos_start();
void mbed_start(void);
void mbed_rtos_init_singleton_mutex(void);
//DOM-IGNORE-BEGIN
#ifdef __cplusplus
}
#endif
//DOM-IGNORE-END
#endif

#endif //__MBED_CONFIG_DATA__
