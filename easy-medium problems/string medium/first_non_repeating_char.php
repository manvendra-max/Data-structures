<?php

//First non repeating character
function firstNonRepeatChar(String $str): String
{
    $strLen = strlen($str);

    if ($strLen == 1) {
        return $str;
    }

    $countMap = [];

    for ($i = 0; $i <= $strLen -1; $i++) {
        if (isset($countMap[$str[$i]])) {
            $countMap[$str[$i]]++;
        } else {
            $countMap[$str[$i]] = 1;
        }
    }
    foreach($countMap as $char=>$count) {
        if ($count == 1) {
            return $char;
        }
    }

    return "No repleating character found";
}

print_r(firstNonRepeatChar("mddwwhheello"));


