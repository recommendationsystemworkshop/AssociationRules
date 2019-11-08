from efficient_apriori import apriori
transactions = [('milk', 'butter', 'cheese'),
                ('milk', 'butter'),
                ('bread', 'butter'),
                ('bread', 'butter')
                ]
itemsets, rules = apriori(transactions, min_support=0.5,  min_confidence=1)
print(rules)  # [{eggs} -> {bacon}, {soup} -> {bacon}]
