# SanDateTime

This is a repository for managing Persian date-time.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install sandatetime.

```bash
pip install sandatetime
```

## Usage

```python
import sandatetime

# returns current Jalali Datetime
sandatetime.now
>> JalaliDateTime(1400, 9, 19, 10, 23, 8, 29496, tzinfo=<DstTzInfo 'Asia/Tehran' +0330+3:30:00 STD>)
```

```python
# returns 5 days ago's starting Jalali date epoch
sandatetime.back_days_epoch(5)
>> 1638649800000
```

```python
# returns converted date from epoch to Jalali
sandatetime.epoch_to_jalali(1638649800000)
>> JalaliDateTime(1400, 9, 14, 0, 0, tzinfo=<DstTzInfo 'Asia/Tehran' +0330+3:30:00 STD>)
```

```python
# returns corresponding standard python datetime object for a Jalali Datetime
sandatetime.jalali_to_gregorian(sandatetime.epoch_to_jalali(1638649800000))
>> datetime.date(2021, 12, 5)
```


## License
[MIT](https://choosealicense.com/licenses/mit/)


