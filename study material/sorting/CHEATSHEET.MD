Colons can be used to align columns.

| Sorting Algorithm name        | Time Complexity           | Space Complexity    |    Stability?           | Sorting Class Type        |
| ----------------------------- |:-------------------------:|:-------------------:|:-----------------------:|--------------------------:|
| Sorting Algorithm name        | Best Case | Avg Case | worst case | worst case  |
| ----------------------------- |:-------------------------:|:-------------------:|:-----------------------:|--------------------------:|
| col 3 is      | right-aligned | $1600 |               | Tables        | Are           | Cool  |
| col 2 is      | centered      |   $12 |               | Tables        | Are           | Cool  |
| zebra stripes | are neat      |    $1 |               | Tables        | Are           | Cool  |
| Tables        | Are           | Cool  |               | Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|               | Tables        | Are           | Cool  |
| col 3 is      | right-aligned | $1600 |               | Tables        | Are           | Cool  |
| col 2 is      | centered      |   $12 |               | Tables        | Are           | Cool  |
| zebra stripes | are neat      |    $1 |               | Tables        | Are           | Cool  |
There must be at least 3 dashes separating each header cell.
The outer pipes (|) are optional, and you don't need to make the 
raw Markdown line up prettily. You can also use inline Markdown.

Markdown | Less | Pretty
--- | --- | ---
*Still* | `renders` | **nicely**
1 | 2 | 3


<table>
    <thead>
        <tr>
            <th rowspan=2>Sorting Algorithm name  </th>
            <th>Time Complexity</th>
            <th>Space Complexity</th>
            <th rowspan=2>Stability?</th>
            <th rowspan=42>Sorting Class Type</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>L1 Name</td>
            <td>L2 Name A</td>
            <td>L3 Name A</td>
        </tr>
        <tr>
            <td>L3 Name B</td>
        </tr>
        <tr>
            <td rowspan=2>L2 Name B</td>
            <td>L3 Name C</td>
        </tr>
        <tr>
            <td>L3 Name D</td>
        </tr>
    </tbody>
</table>