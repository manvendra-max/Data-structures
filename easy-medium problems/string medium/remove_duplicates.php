<?php

use FFI\CType;
function removeDups($str)
{
    $countMap = [];
    $resultStr = '';

    for ($i = 0; $i <= strlen($str)-1; $i++) {
        $countMap[$str[$i]] = ($countMap[$str[$i]] ?? 0) + 1;
        
        if ($countMap[$str[$i]] === 1) {
            $resultStr .= $str[$i];
        }
    }
    return  $resultStr;
}

print_r(removeDups("aacaabnmn mnmm"));
