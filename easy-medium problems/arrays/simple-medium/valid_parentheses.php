<?php
function checkValidParantheses(array $arr)
{
    $stack = [];
    $len = count($arr);

    // (){}[]
    $map = [
        ')' => '(',
        ']' => '[',
        '}' => '{',
    ];

    for ($i = 0; $i < $len; $i++) {
        $char = $arr[$i];

        if (in_array($char, ['(', '[', '{'])) {
            $stack[] = $char;
        } else {
            $top = array_pop($stack);
            if ($top !== $map[$char]) {
                return false;
            }
        }
    }
    if (empty($stack)) {
        return true;
    }
    return false;
}

print_r(checkValidParantheses(['[','(', ')', '{', '}', '[', ']', ']' ]));
