#!/usr/bin/python
import  RPi.GPIO as GPIO   # Para acceder a GPIO
import time                # Para esperar entre parpadeos
"""
Este script demuestra el uso de RPi.GPIO para hacer parpadear un LED
setup:
El LED esta conectado a la pata 11 (fisica)
python blink11.py
Se debe ver parpadear el LED
Se sale del programa con ctrl+C
"""
LED_PIN = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.output(LED_PIN, 0)  

ledState = False               # El LED esta inicialmente apagado
# Lazo infinito
try:
    while True:
        if ledState == False:
        # LED esta apagado,prenderlo
            GPIO.output(LED_PIN, 1) 
            ledState = True        # LED prendido
        else:
            GPIO.output(LED_PIN,0)
            ledState = False
        print "LED prendido?\nAns: %s" %(ledState)
    # Esperar un tiempo 
        time.sleep(1)
except KeyboardInterrupt:  
    GPIO.cleanup()         # Limpiando
