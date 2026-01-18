<?php

function printStr($str)
{
    print_r($str);
    // return $str;
}

function stringToAscii($str) {
    return array_map('ord'
    , str_split($str));
}
print_r(stringToAscii("ABCa1")); // [65,66,67]


