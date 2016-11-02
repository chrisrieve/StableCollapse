use "data.dta", clear
describe
egen total = total(*)
collapse (sum) value, by(year month day)
