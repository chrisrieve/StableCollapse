use "data.dta", clear
* Hey There! Just a friendly reminder to ALWAYS SORT STABLY.
sort year sku, stable
describe
egen total = total(*)
* Hey There! Just a friendly reminder to ALWAYS SORT STABLY.
sort year month day, stable
collapse (sum) value, by(year month day)
gen white = (blue == 0)
* Hey There! Just a friendly reminder to ALWAYS SORT STABLY.
sort year month, stable
collapse (sum) value, by(year month)
