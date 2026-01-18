<?php
// If one string can be rearranged and become another one then both strings are aragrams

function areAnagram(String $s1, String $s2)
{

    $s1 = str_split(strtolower(($s1)));
    $s2 = str_split(strtolower(($s2)));
    
    sort($s1); //sort return boolean
    sort($s2);

    if ($s1 == $s2) {
        return true;
    }
    return false;

}

$s1 = 'Earth';

$s2 = 'Heart@e';

// print_r(areAnagram($s1, $s2));


// optimised apprach
function areAnagramOptimized($s1, $s2)
{
    $s1 = strtolower(preg_replace('/[^a-z0-9]/i', '', $s1));
    $s2 = strtolower(preg_replace('/[^a-z0-9]/i', '', $s2));

    if (strlen($s1) != strlen($s2)) {
        return "false";
    }

    $count = [];

    for ($i = 0; $i <= strlen($s1)-1; $i++)
        {
            $count[$s1[$i]] = ($count[$s1[$i]] ?? 0) + 1;
            $count[$s2[$i]] = ($count[$s2[$i]] ?? 0) - 1;
        }
    
    foreach ($count as $freq) {
        if ($freq != 0) {
            return "false";
        }
    }
    return true;
}

print_r(areAnagramOptimized($s1, $s2));




