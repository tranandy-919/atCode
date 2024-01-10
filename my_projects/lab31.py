#!/usr/bin/env python3
def main():
    wordbank= ["indentation", "spaces", 4]
    tlgstudents= ['Albert', 'Anthony', 'Brenden', 'Craig', 'Deja', 'Elihu', 'Eric', 'Giovanni', 'James', 'Joshua', 'Maria', 'Mohamed', 'PJ', 'Philip', 'Sagan', 'Suchit', 'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping']
    wordbank.append(4)
    num = int(input("Pick a student! 0 - 20: "))
    student = tlgstudents[num]
    print(f"{student} always uses {wordbank[2]} {wordbank[1]} for {wordbank[0]}.")
main()
