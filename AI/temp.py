class PredictiveParsingTable:
    def __init__(self, grammar):
        self.grammar = grammar
        self.non_terminals = grammar.keys()
        self.terminals = set()
        self.parsing_table = {}

        for productions in grammar.values():
            for production in productions:
                for symbol in production:
                    if symbol not in self.non_terminals:
                        self.terminals.add(symbol)

        for non_terminal in self.non_terminals:
            self.parsing_table[non_terminal] = {}

        for non_terminal, productions in grammar.items():
            for production in productions:
                first_set = self.compute_first_set(production)
                for terminal in first_set:
                    self.parsing_table[non_terminal][terminal] = production

                if '' in first_set:
                    follow_set = self.compute_follow_set(non_terminal)
                    for terminal in follow_set:
                        self.parsing_table[non_terminal][terminal] = production

    def compute_first_set(self, production):
        first_set = set()
        symbol = production[0]
        if symbol in self.terminals:
            first_set.add(symbol)
        else:
            first_set.update(self.compute_first_set(self.grammar[symbol][0]))

        return first_set

    def compute_follow_set(self, non_terminal):
        follow_set = set()
        if non_terminal == 'S':
            follow_set.add('$')

        for nt, productions in self.grammar.items():
            for production in productions:
                if non_terminal in production:
                    idx = production.index(non_terminal)
                    if idx < len(production) - 1:
                        follow_set.update(self.compute_first_set(production[idx + 1:]))
                    elif idx == len(production) - 1:
                        if nt != non_terminal:
                            follow_set.update(self.compute_follow_set(nt))

        return follow_set

    def print_parsing_table(self):
        for non_terminal, terminals in self.parsing_table.items():
            print(f'Non-terminal {non_terminal}:')
            for terminal, production in terminals.items():
                print(f'  Terminal {terminal}: {production}')


# Grammar G1: S->AaDd|DdDa
grammar_g1 = {
    'S': ['AaDd', 'DdDa'],
    'A': ['a'],
    'D': ['d']
}

# Grammar G2: AaBaAbBb|BbAaBaAb
grammar_g2 = {
    'S': ['AaBaAbBb', 'BbAaBaAb'],
    'A': ['a'],
    'B': ['b']
}

pp_table_g1 = PredictiveParsingTable(grammar_g1)
pp_table_g2 = PredictiveParsingTable(grammar_g2)

print("Predictive Parsing Table for Grammar G1:")
pp_table_g1.print_parsing_table()

print("\nPredictive Parsing Table for Grammar G2:")
pp_table_g2.print_parsing_table()
