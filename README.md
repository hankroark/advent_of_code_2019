# Advent of Code 2019

## Deploy this to Cloud Run
[![Run on Google Cloud](https://deploy.cloud.run/button.svg)](https://deploy.cloud.run?dir=src)

## How to use the APIs

All APIs if successful, return a JSON file with the Part 1 and Part 2 answers.

Example JSON will be:
```
{ 
 'part1': result1,
 'part2': result2
}
```

### Day 01
`http://hostname/day01`

For example `curl -i -X POST -H "Content-Type: multipart/form-data" -F "file=@input_fuel_counter.txt" http://localhost:8080/day01`

### Day 02
`http://hostname/day02/program/target`

For example `curl http://localhost:8080/day02/1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,2,19,9,23,1,23,5,27,2,6,27,31,1,31,5,35,1,35,5,39,2,39,6,43,2,43,10,47,1,47,6,51,1,51,6,55,2,55,6,59,1,10,59,63,1,5,63,67,2,10,67,71,1,6,71,75,1,5,75,79,1,10,79,83,2,83,10,87,1,87,9,91,1,91,10,95,2,6,95,99,1,5,99,103,1,103,13,107,1,107,10,111,2,9,111,115,1,115,6,119,2,13,119,123,1,123,6,127,1,5,127,131,2,6,131,135,2,6,135,139,1,139,5,143,1,143,10,147,1,147,2,151,1,151,13,0,99,2,0,14,0/19690720`

### Day 04
`http://hostname/day04/start_password/end_password`

For example `curl http://localhost:8080/day04/240298/784956`
