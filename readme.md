---
title: Harmony 3 MBED OS RTOS configurations and template files
nav_order: 1
has_children: true
has_toc: false
---
[![MCHP](https://www.microchip.com/ResourcePackages/Microchip/assets/dist/images/logo.png)](https://www.microchip.com)

# Harmony 3 MBED OS RTOS configurations and template files

MPLAB® Harmony 3 is an extension of the MPLAB® ecosystem for creating embedded firmware solutions for Microchip 32-bit SAM and PIC® microcontroller and microprocessor devices.  Refer to the following links for more information.

- [Microchip 32-bit MCUs](https://www.microchip.com/design-centers/32-bit)
- [Microchip 32-bit MPUs](https://www.microchip.com/design-centers/32-bit-mpus)
- [Microchip MPLAB X IDE](https://www.microchip.com/mplab/mplab-x-ide)
- [Microchip MPLAB® Harmony](https://www.microchip.com/mplab/mplab-harmony)
- [Microchip MPLAB® Harmony Pages](https://microchip-mplab-harmony.github.io/)

This repository contains MPLAB Harmony 3 MBED OS RTOS configurations and template files. Mbed OS RTOS source code is not included in this repository and must be downloaded separately.
Refer to the following links for release notes, training materials, and license
information and source code
 - [Release Notes](./release_notes.md)
 - [MPLAB® Harmony License](mplab_harmony_license.md)

# Contents Summary

| Folder    | Description                                                |
|-----------|------------------------------------------------------------|
| config    | Mbed OS RTOS module configuration scripts                  |
| templates | Mbed OS RTOS and system file templates                     |
| docs      | Contains documentation in html format for offline viewing (to be used only after cloning this repository onto a local machine). Use [github pages](https://microchip-mplab-harmony.github.io/mbed_os_rtos/) of this repository for viewing it online.                            |

# Harmony 3 MBED OS RTOS
Harmony 3 Mbed OS RTOS is an RTOS which includes an RTX and all RTOS APIs. It supports deterministic, multithreaded and real-time software execution. The RTOS primitives are always available, allowing drivers and applications to rely on threads, semaphores, mutexes and other RTOS features.

Harmony 3 Mbed OS RTOS example applications are available at [mbed_os_rtos_apps](https://github.com/Microchip-MPLAB-Harmony/mbed_os_rtos_apps)

The following RTOS APIs are supported in Harmony 3 Mbed OS RTOS:

| Mbed OS RTOS API |
|------------------|
| [ConditionVariable](https://os.mbed.com/docs/mbed-os/v6.7/apis/rtos-apis.html) |
| [EventFlags](https://os.mbed.com/docs/mbed-os/v6.7/apis/eventflags.html) |
| [Idle loop](https://os.mbed.com/docs/mbed-os/v6.7/apis/idle-loop.html) |
| [Kernel interface functions](https://os.mbed.com/docs/mbed-os/v6.7/apis/kernel-interface-functions.html) |
| [Mail](https://os.mbed.com/docs/mbed-os/v6.7/apis/mail.html) |
| [Mutex](https://os.mbed.com/docs/mbed-os/v6.7/apis/mutex.html) |
| [Queue](https://os.mbed.com/docs/mbed-os/v6.7/apis/queue.html) |
| [Semaphore](https://os.mbed.com/docs/mbed-os/v6.7/apis/semaphore.html) |
| [ThisThread](https://os.mbed.com/docs/mbed-os/v6.7/apis/thisthread.html) |
| [Thread](https://os.mbed.com/docs/mbed-os/v6.7/apis/thread.html) |

Refer the following links for more information:
 - [Mbed OS RTOS API documentation](https://os.mbed.com/docs/mbed-os/v6.7/apis/rtos-apis.html)
 - [Mbed OS License information](https://os.mbed.com/docs/mbed-os/v6.7/contributing/license.html)

____

[![License](https://img.shields.io/badge/license-Harmony%20license-orange.svg)](https://github.com/Microchip-MPLAB-Harmony/mbed_os_rtos/blob/master/mplab_harmony_license.md)
[![Latest release](https://img.shields.io/github/release/Microchip-MPLAB-Harmony/mbed_os_rtos.svg)](https://github.com/Microchip-MPLAB-Harmony/mbed_os_rtos/releases/latest)
[![Latest release date](https://img.shields.io/github/release-date/Microchip-MPLAB-Harmony/mbed_os_rtos.svg)](https://github.com/Microchip-MPLAB-Harmony/mbed_os_rtos/releases/latest)
[![Commit activity](https://img.shields.io/github/commit-activity/y/Microchip-MPLAB-Harmony/mbed_os_rtos.svg)](https://github.com/Microchip-MPLAB-Harmony/mbed_os_rtos/graphs/commit-activity)
[![Contributors](https://img.shields.io/github/contributors-anon/Microchip-MPLAB-Harmony/mbed_os_rtos.svg)]()

____

[![Follow us on Youtube](https://img.shields.io/badge/Youtube-Follow%20us%20on%20Youtube-red.svg)](https://www.youtube.com/user/MicrochipTechnology)
[![Follow us on LinkedIn](https://img.shields.io/badge/LinkedIn-Follow%20us%20on%20LinkedIn-blue.svg)](https://www.linkedin.com/company/microchip-technology)
[![Follow us on Facebook](https://img.shields.io/badge/Facebook-Follow%20us%20on%20Facebook-blue.svg)](https://www.facebook.com/microchiptechnology/)
[![Follow us on Twitter](https://img.shields.io/twitter/follow/MicrochipTech.svg?style=social)](https://twitter.com/MicrochipTech)

[![](https://img.shields.io/github/stars/Microchip-MPLAB-Harmony/mbed_os_rtos.svg?style=social)]()
[![](https://img.shields.io/github/watchers/Microchip-MPLAB-Harmony/mbed_os_rtos.svg?style=social)]()