# Advent of Code 2019

## Deploy this to Cloud Run
[![Run on Google Cloud](https://deploy.cloud.run/button.svg)](https://deploy.cloud.run?dir=src)

## How to use the APIs

All APIs if successful, return a JSON file with the Part 1 and Part 2 answers.

Example JSON will be:
```
{ 'part1': result1,
  'part2': result2
}
```

### Day 01
`http://hostname/day01`

For example `curl -i -X POST -H "Content-Type: multipart/form-data" -F "file=@input_fuel_counter.txt" http://localhost:8080/day01`

### Day 04
`http://hostname/day04/start_password/end_password`

For example `curl http://localhost:8080/day04/240298/784956`
