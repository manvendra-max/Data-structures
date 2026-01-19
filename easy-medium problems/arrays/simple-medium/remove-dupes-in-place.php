<?php

//here we are removing the elemenets from the sorted array
function removeDupes(array $arr)
{
    $i = 0;

    $arrLen = count($arr);
    
    for($j = 1; $j<= $arrLen-1; $j++) {
        if ($arr[$i] != $arr[$j]) {
            $i += 1;
            $arr[$i] = $arr[$j];
        }
    }

    return array_splice($arr, 0, $i+1);
}

print_r(removeDupes([1,2,2,3,4,5,5,6]));



