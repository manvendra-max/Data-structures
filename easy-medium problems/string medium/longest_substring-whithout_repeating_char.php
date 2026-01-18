<?php

// brutforce solution with O(n^2) time complexity
function longestSubString(string $str): string
{
    // $str = 'abcdadbmn';

    if (strlen($str) === 1) {
        return $str;
    }
    $longestString = '';

    for ($i = 0; $i <= strlen($str) - 1; $i++) {
        $frequencyMap = [];
        $tempStr = '';

        for ($j = $i; $j <= strlen($str) - 1; $j++) {

            if (isset($frequencyMap[$str[$j]])) {
                break;
            } else {
                // print_r($str[$j]);
                $tempStr .= $str[$j];
                $frequencyMap[$str[$j]] = true;
            }
        }

        if (strlen($tempStr) > strlen($longestString)) {
            $longestString = $tempStr;
        }
    }
    return $longestString;
}

print_r(longestSubString('abcabcbb'));


/**
 * Optimised approach
*/
function longestSubStrOptimized(String $str)
{
    //str = "abcdanml"

    $idxCounterMap = [];
    $result = 0;

    $right = 0;
    $left = 0;

    $strLen = strlen($str);

    while($right < $strLen) {
        
        if (isset($idxCounterMap[$str[$right]]) && $idxCounterMap[$str[$right]] >= $left) {
            $left = $idxCounterMap[$str[$right]] + 1;
        }
        
        $idxCounterMap[$str[$right]] = $right;

        if (($right - $left + 1 ) > $result) {
            $result = $right - $left + 1;
        }

        $right += 1;
    }
    return $result;

}

print_r(longestSubStrOptimized("abcamlkmna"));





