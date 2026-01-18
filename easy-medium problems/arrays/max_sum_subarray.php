<?php

function maxSubArrSum(array $arr)
{
    // [1,-1,2,3,-6,1,2,3]

    $maxSum = PHP_INT_MIN;

    $sum = 0;
    $right = $left = $tempLeft = 0;

    
    for($i = 0; $i<= count($arr)-1; $i++) {
        
        $sum += $arr[$i];
        if ($sum >= $maxSum) {
            $maxSum = $sum;

            $right = $i;
            $left = $tempLeft;

        }

        if ($sum < 0) {
            $sum = 0;
            $tempLeft = $i+1;
        }
    }

    return [
        "Sum" => $maxSum,
        "array" => array_slice($arr, $left, $right-$left+1)
    ];
}

print_r(maxSubArrSum([1,-1,2,-3,6,1,2,3]));



