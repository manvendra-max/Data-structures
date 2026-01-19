<?php
function moveZeroesToEnd(array $arr): array
{
    $len = count($arr);

    $left = -1;

    for ($i = 0; $i <= $len-1; $i++) {
        if ($arr[$i] === 0) {
            $left = $i;
            break;
        }
    }
    if ($left === -1) {
        return $arr;
    }
    for ($right = $left; $right <= $len-1; $right++) {
        if ($arr[$right] != 0) {
            swap($arr, $right, $left);
            $left++;
        }
    }
    return $arr;

}

function swap(array &$arr, $idx1, $idx2)
{
    $temp = $arr[$idx1];

    $arr[$idx1] = $arr[$idx2];
    $arr[$idx2] = $temp;
}

print_r(moveZeroesToEnd([1,0,0,7,0,6,0,8]));
