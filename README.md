# Omo Simulator 

## Credits

A few weeks ago, I found an “omorashi-themed game” - *[A Long Hour and a Half](https://github.com/OmoExplorer/long-hour-and-a-half)*, and got inspired. I thought its omo simulating system is great, so I extract the core omo part, mainly contains absorbing, peeing, leaking, etc. 

***So give our highest thanks to the rightful author [@OmoExplorer](https://github.com/OmoExplorer) first!***

## Setup

### Python 3.11+

This project requires **Python 3.11+**.

To check your Python version, open terminal and run:

```sh
python --version
```

The following text should be on your screen:

```
Python 3.11.4
```

### Dependencies

This project requires the following Python libraries:

 - click == 8.1.7
 - colorama == 0.4.6
 - termcolor == 2.4.0

To install these dependencies, navigate to your project's directory and run the following command:

```sh
pip install -r requirements.txt
```

## Run

Start the simulator:

```sh
python ./src/main.py
```

### Options

```sh
python ./src/main.py --help
```

```
Usage: main.py [OPTIONS]

  Start simulating.

Options:
  -c, --config FILENAME           [default: (./src/Jane.json)]
  -t, --time [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]
                                  [default: (Now)]
  -b, --bladder INTEGER           [default: (0)]
  --help                          Show this message and exit.
```

### Actions

| NAME   | ARG         | DOCUMENT                                                                        |
| :----- | :---------- | :------------------------------------------------------------------------------ |
| drink  | volume(int) | Drink certain amount of water into stomach.                                     |
| toilet | ---         | Use the toilet and empty the bladder.                                           |
| hold   | ---         | Do hold to increase sphincter power, like rubbing tights or pressing on crotch. |

### Example

(cls is turned off)
```
$ python ./src/main.py --time "2022-2-14 12:04:16" --bladder 700
Jane's 02/14/2022 12:04 PM
 Fullness: 77.7% (700/900.0)  // bursting
 Power: 100%
 Tummy: 0
 Clothes: Underwear( 14.0 ) | Outerwear( 42.0 )
> drink 300  // drink 300mL
Jane's 02/14/2022 12:06 PM
 Fullness: 78.5% (707/900.0)
 Power: 96.8%
 Tummy: 297
 Clothes: Underwear( 13.0 ) | Outerwear( 42.0 )  // leaked
>  // do nothing by just pressing enter without inputting anything
Jane's 02/14/2022 12:08 PM
 Fullness: 79.5% (716/900.0)
 Power: 93.6%
 Tummy: 294
 Clothes: Underwear( 13.0 ) | Outerwear( 42.0 )
> hold  // do hold
Jane's 02/14/2022 12:10 PM
 Fullness: 80.4% (724/900.0)
 Power: 96.7%  // sphincter power increased because of holding above
 Tummy: 291
 Clothes: Underwear( 13.0 ) | Outerwear( 42.0 )
> hold  // do hold again
Jane's 02/14/2022 12:12 PM
 Fullness: 81.4% (733/900.0)
 Power: 96.7%
 Tummy: 288
 Clothes: Underwear( 13.0 ) | Outerwear( 42.0 )
>  // do nothing by just pressing enter without inputting anything
Jane's 02/14/2022 12:14 PM
 Fullness: 82.3% (741/900.0)
 Power: 93.4%
 Tummy: 285
 Clothes: Underwear( 13.0 ) | Outerwear( 42.0 )
> toilet  // release!
Jane's 02/14/2022 12:16 PM
 Fullness: 1.0% (9/900.0)
 Power: 97.4%
 Tummy: 282
 Clothes: Underwear( 14.0 ) | Outerwear( 42.0 )
>  // waiting for you to control
```

## Configuration 

| NAME                        | TYPE   | VALUE/RANGE    |
| :-------------------------- | :----- | :------------- |
| name                        | string | ---            |
| gender                      | string | male/female    |
| age                         | int    | x >= 0         |
| maximal_urine               | int    | x > 0          |
| urine_income_bounds         | array  | [x > 0, y > x] |
| min_sphincter_leaking_power | int    | 100 >= x > 0   |
| leak_volume_bounds          | array  | [x > 0, y > x] |
| embarrassment_decay         | float  | 100 >= x >= 0  |
| thirst_increase             | int    | x >= 0         |
| wear.name                   | string | ---            |
| wear.pressure               | int    | ---            |
| wear.absorption             | float  | x >= 0         |
| wear.drying                 | float  | x >= 0         |

## Further thoughts

### More details

Peeing for given seconds, peeing in a cup, different power increasing with different actions are all the things to be completed. I'm a middle school student so I don't really have much time. It's the best if you can contribute!

### Preciser mechanisms

Hydration is complex. This omo system is quite inaccurate in my opinion. I am still reading some papers on body hydration to figure out how it works and what factors may effect them. If you know anything would you like to [contribute](#contributing)?

## Contributing

Contributions, issues, and feature requests are welcome! 

Contact me at [omo.jian@proton.me](omo.jian@proton.me) if you have any ideas. 
