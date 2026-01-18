<?php

// Reverse whole string

$st = "hello My name is   Manvendra";
$rev = '';

for ($i = strlen($st) - 1 ; $i >= 0; $i--) {
    $rev .= $st[$i];
}

// print_r($rev);


//reverse the sentance but words should remain same

$stArray = explode(' ', $st);
print_r( $stArray);
$revSentence = '';

for ($i = count($stArray) - 1; $i >= 0 ; $i--) {
    $revSentence .= $stArray[$i] . ' ';
}
// print_r(trim($revSentence));


//palindrome

$palindrome = "9@i  uiu  i !9";

$temp = strtolower(preg_replace('/[^a-z0-9]/i', '',$palindrome));

print_r($temp == strrev($temp));

// Palindrome optimised version

function isPalindrome(String $str)
{

    $palindrome = $str;
    $left = 0;
    $right = strlen($palindrome) - 1;
    
    while ($left < $right) {
        
        while($left < $right && !ctype_alnum($palindrome[$left])) {
            $left++;
        }
    
        while($left < $right && !ctype_alnum($palindrome[$right])) {
            $right--;
        }
        if ($palindrome[$left] != $palindrome[$right]) {
            return false;
        }

        $left++;
        $right--;
    }

    return true;
}

print_r(isPalindrome("9@i  uiu  i !9"));

