#!/usr/bin/env python3
"""
ESP32-CYD Firmware Setup Script
Creates the firmware directory structure with base firmware and templates
"""

import os
import json

def create_firmware_directory():
    # Create the main firmware directory structure
    firmware_dirs = [
        'firmware',
        'firmware/odroid_go_base',
        'firmware/odroid_go_base/lib',
        'firmware/odroid_go_base/include',
        'firmware/odroid_go_base/src',
        'firmware/odroid_go_base/data',
        'firmware/esp-idf_boilerplate',
        'firmware/esp-idf_boilerplate/main',
        'firmware/platformio_template',
        'firmware/platformio_template/src',
        'firmware/platformio_template/include',
        'firmware/platformio_template/lib'
    ]
    
    for directory in firmware_dirs:
        os.makedirs(directory, exist_ok=True)
        print(f"Created directory: {directory}")
    
    # Create Odroid-Go base firmware files
    create_odroid_go_base()
    
    # Create ESP-IDF boilerplate
    create_esp_idf_boilerplate()
    
    # Create PlatformIO template
    create_platformio_template()
    
    print("\nFirmware directory structure created successfully!")
    print("Next steps:")
    print("1. Add actual compiled firmware binaries")
    print("2. Customize the templates for your specific hardware")
    print("3. Add documentation for building and flashing")

def create_odroid_go_base():
    # Main application file for Odroid-Go base
    main_app_content = """#include <stdio.h>
#include <freertos/FreeRTOS.h>
#include <freertos/task.h>
#include <esp_system.h>
#include <odroid_go.h>

void app_main(void)
{
    // Initialize ODROID-GO hardware
    GO.begin();
    
    // Clear screen
    GO.lcd.clear();
    GO.lcd.setCursor(0, 0);
    GO.lcd.setTextSize(2);
    GO.lcd.setTextColor(WHITE);
    
    // Display welcome message
    GO.lcd.println("ESP32-CYD Launcher");
    GO.lcd.println("-----------------");
    GO.lcd.setTextSize(1);
    GO.lcd.println("Base Firmware v1.0");
    GO.lcd.println("Ready...");
    
    // Simple menu system
    while(1) {
        GO.update();
        
        if (GO.BtnA.isPressed()) {
            GO.lcd.clear();
            GO.lcd.setCursor(0, 0);
            GO.lcd.setTextSize(2);
            GO.lcd.println("Button A Pressed");
            vTaskDelay(1000 / portTICK_PERIOD_MS);
            GO.lcd.clear();
            GO.lcd.setCursor(0, 0);
            GO.lcd.println("ESP32-CYD Launcher");
            GO.lcd.println("-----------------");
        }
        
        if (GO.BtnB.isPressed()) {
            GO.lcd.clear();
            GO.lcd.setCursor(0, 0);
            GO.lcd.setTextSize(2);
            GO.lcd.println("Button B Pressed");
            vTaskDelay(1000 / portTICK_PERIOD_MS);
            GO.lcd.clear();
            GO.lcd.setCursor(0, 0);
            GO.lcd.println("ESP32-CYD Launcher");
            GO.lcd.println("-----------------");
        }
        
        vTaskDelay(10 / portTICK_PERIOD_MS);
    }
}
"""
    
    with open('firmware/odroid_go_base/src/main.c', 'w') as f:
        f.write(main_app_content)
    
    # Component.mk file
    component_mk_content = """#
# Component makefile for odroid_go_base
#
COMPONENT_ADD_INCLUDEDIRS := include
COMPONENT_SRCDIRS := src
"""
    
    with open('firmware/odroid_go_base/component.mk', 'w') as f:
        f.write(component_mk_content)
    
    # Makefile
    makefile_content = """PROJECT_NAME := odroid_go_base
include $(IDF_PATH)/make/project.mk
"""
    
    with open('firmware/odroid_go_base/Makefile', 'w') as f:
        f.write(makefile_content)
    
    # README with build instructions
    readme_content = """# ODROID-GO Base Firmware

This is the base firmware for the ESP32-CYD, adapted from the ODROID-GO hardware.

## Building the Firmware

1. Set up the ESP-IDF environment
2. Change to this directory
3. Run `make menuconfig` to configure the project
4. Run `make` to build the firmware
5. Flash using `make flash` or esptool.py

## Features

- Basic display driver for the LCD
- Input handling for buttons
- Simple menu system
- Foundation for more complex applications

## Hardware Support

- ILI9341 LCD display
- Button inputs (A, B, Start, Select)
- SD card slot
- Speaker output
- Battery monitoring
"""
    
    with open('firmware/odroid_go_base/README.md', 'w') as f:
        f.write(readme_content)

def create_esp_idf_boilerplate():
    # Main application file for ESP-IDF boilerplate
    main_app_content = """#include <stdio.h>
#include <freertos/FreeRTOS.h>
#include <freertos/task.h>
#include <esp_system.h>
#include <driver/gpio.h>
#include <esp_log.h>

// Include your display library here
// #include "ili9341.h"

#define TAG "ESP32-CYD-App"

void app_main(void)
{
    ESP_LOGI(TAG, "Starting ESP32-CYD application!");
    
    // Initialize your display here
    // display_init();
    
    while(1) {
        ESP_LOGI(TAG, "Hello from ESP32-CYD!");
        vTaskDelay(1000 / portTICK_PERIOD_MS);
    }
}
"""
    
    with open('firmware/esp-idf_boilerplate/main/main.c', 'w') as f:
        f.write(main_app_content)
    
    # CMakeLists.txt for ESP-IDF
    cmake_content = """# CMakeLists.txt for ESP32-CYD Boilerplate

idf_component_register(SRCS "main.c"
                    INCLUDE_DIRS "."
                    REQUIRES )"""
    
    with open('firmware/esp-idf_boilerplate/main/CMakeLists.txt', 'w') as f:
        f.write(cmake_content)
    
    # Top-level CMakeLists.txt
    top_cmake_content = """# The following lines of boilerplate have to be in your project's
# CMakeLists in this exact order for cmake to work correctly
cmake_minimum_required(VERSION 3.5)

include($ENV{IDF_PATH}/tools/cmake/project.cmake)
project(esp32_cyd_boilerplate)"""
    
    with open('firmware/esp-idf_boilerplate/CMakeLists.txt', 'w') as f:
        f.write(top_cmake_content)
    
    # README with instructions
    readme_content = """# ESP-IDF Boilerplate for ESP32-CYD

This is a boilerplate template for creating applications for the ESP32-CYD using the ESP-IDF framework.

## Getting Started

1. Set up the ESP-IDF environment
2. Copy this template to your project directory
3. Update the CMakeLists.txt files as needed
4. Add your application code to main.c
5. Configure your project with `idf.py menuconfig`
6. Build with `idf.py build`
7. Flash with `idf.py flash`

## Project Structure

- `main/` - Main application source code
  - `main.c` - Main application entry point
  - `CMakeLists.txt` - Component build instructions
- `CMakeLists.txt` - Project build instructions

## Adding Components

To add components (like display drivers):
1. Create a components directory
2. Add your component there
3. Update the main CMakeLists.txt to include the components directory
"""
    
    with open('firmware/esp-idf_boilerplate/README.md', 'w') as f:
        f.write(readme_content)

def create_platformio_template():
    # PlatformIO project configuration
    platformio_ini = """[env:esp32-cyd]
platform = espressif32
board = esp32dev
framework = espidf
monitor_speed = 115200

# Custom upload port if needed
; upload_port = /dev/ttyUSB0

# Build flags
build_flags = 
    -D CONFIG_ESP32_DEFAULT_CPU_FREQ_240=1
    -D CONFIG_FREERTOS_HZ=100

# Library dependencies
lib_deps = 
    ; Add display libraries here
    ; bodmer/TFT_eSPI@^2.5.0
"""
    
    with open('firmware/platformio_template/platformio.ini', 'w') as f:
        f.write(platformio_ini)
    
    # Main application file for PlatformIO
    main_app_content = """#include <Arduino.h>
// Include your display library here
// #include <TFT_eSPI.h>

// TFT_eSPI tft;

void setup() {
  Serial.begin(115200);
  
  // Initialize your display here
  // tft.init();
  // tft.setRotation(1);
  // tft.fillScreen(TFT_BLACK);
  // tft.setTextColor(TFT_WHITE, TFT_BLACK);
  // tft.println("ESP32-CYD Ready!");
  
  Serial.println("ESP32-CYD PlatformIO Template");
}

void loop() {
  Serial.println("Hello from PlatformIO!");
  delay(1000);
}
"""
    
    with open('firmware/platformio_template/src/main.cpp', 'w') as f:
        f.write(main_app_content)
    
    # README with instructions
    readme_content = """# PlatformIO Template for ESP32-CYD

This is a template for creating applications for the ESP32-CYD using PlatformIO.

## Getting Started

1. Install PlatformIO Core or PlatformIO IDE
2. Copy this template to your project directory
3. Install any required libraries (update platformio.ini)
4. Customize src/main.cpp with your application code
5. Build with `pio run`
6. Upload with `pio run --target upload`

## PlatformIO.ini Configuration

The platformio.ini file is configured for:
- ESP32 Dev Module board
- ESP-IDF framework
- Serial monitor at 115200 baud

## Adding Libraries

To add libraries:
1. Search for libraries in the PlatformIO registry
2. Add them to the `lib_deps` section in platformio.ini
3. Run `pio run` to automatically install them

## Common Commands

- `pio run` - Build the project
- `pio run --target upload` - Build and upload
- `pio run --target clean` - Clean the build
- `pio device monitor` - Serial monitor
"""
    
    with open('firmware/platformio_template/README.md', 'w') as f:
        f.write(readme_content)

if __name__ == "__main__":
    create_firmware_directory()
