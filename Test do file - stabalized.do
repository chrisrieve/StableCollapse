use "data.dta", clear
describe
egen total = total(*)
* Hey There! Just a friendly reminder to ALWAYS SORT STABLY.
sort year month day, stable
collapse (sum) value, by(year month day)
