#!/usr/bin/lua

local ftcsv = require('ftcsv')
local zipcodes, headers = ftcsv.parse("test.csv")

local ftcsv = require("ftcsv")
for zipcodes, headers in ftcsv.parseLine("test.csv") do
    print(zipcode.Zipcode)
    print(zipcode.State)
end