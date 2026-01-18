<?php
// group anagrams from group of string array

function groupAnagram(array $words): array
{
    $result = [];

    foreach ($words as $word) {
        $key = str_split(strtolower($word));

        sort($key);

        $result[implode($key)][] = $word;
    }
    return array_values($result);
}

print_r(groupAnagram(['aba', 'cat', 'baa', 'dog', 'god']));

