use "data.dta", clear
describe
egen total = total(*)
collapse (sum) value, by(year month day)
gen white = (blue == 0)
collapse (sum) value, by(year month)
