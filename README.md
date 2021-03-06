# Конвертор температуры

![develop](https://github.com/ADsty/temperature_convertor/actions/workflows/tests.yml/badge.svg?branch=develop) - develop

![main](https://github.com/ADsty/temperature_convertor/actions/workflows/tests.yml/badge.svg?branch=main) - main

## Описание программы

Программа позволяет переводить температуру в разные единицы измерения. Поддерживаемые единицы измерения: градусы Цельсия,
Кельвины и Фаренгейты.

## Использование программы

Чтобы запустить программу можно использовать команду

```
python temperature_convertor.py
```

Чтобы перевести температуру в другую единицу измерения, необходимо после запуска программы ввести строку вида
`значение` `исходные единицы измерения` `нужные единицы измерения`

Поддерживаемые форматы для единиц измерения: K для Кельвинов, C для градусов Цельсия и F для Фаренгейтов.

Для завершения программы необходимо ввести строку вида `quit`

## Пример использования программы

Перевод 10 градусов Цельсия в Кельвины:

```
Temperature convertor v1.0
To convert temperature type: [value] [initial temperature unit] [needed temperature unit]
To stop the program type 'quit' 
Maintained temperature units are: Kelvin (type as K), Celsius (type as C), Fahrenheit (type as F)
Type what do you want: 10 C K
Your result is 283.15 K
```

## Запуск через Docker

Для запуска программы через Docker необходимо выполнить команду:

```docker build -t temperature_convertor .```

После этого необходимо выполнить команду:

```docker run -it temperature_convertor```