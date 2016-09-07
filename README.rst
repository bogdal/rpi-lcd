rpi-lcd
========

I²C LCD library for RaspberryPi.

.. code-block:: python

    from rpi_lcd import LCD

    lcd = LCD()
    lcd.text('line 1', 1)
    lcd.text('line 2', 2, 'right')
    lcd.text('line 3', 3, 'center')
    lcd.text('line 4', 4)
