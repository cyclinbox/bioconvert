

class edam_manager(object):

    def __init__(self):
        # ontology parsing happens here
        pass

    def get_terms_by_name(self, name):
        """
        query for ontological terms by name
        :param name: str
        :return: collection of term
        """
        pass

    def common_ancestors(self, term1, term2):
        """
        returns the terms that are the least common ancestors of the given two terms
        :param term1:
        :param term2:
        :return: collection of term
        """
        pass

    def is_placeholder(self, term):
        """
        checks if a term is a real term or a placeholder created for structuring purposes.
        :param term:
        :return: True if the term is an organisational entity (e.g., alignment, 'phylogenetic data')
        or False if it is a real term (e.g., 'sequence alignment', 'phylogenetic tree').
        """
        pass

    def format2data(self, term):
        """
        given a format term returns the corresponding data terms, e.g. given 'newick' returns 'phylogenetic tree'.
        :param term: format term
        :return: collection of data term
        """
        pass

    def get_description(self, term):
        """
        returns the term description
        :param term:
        :return: str
        """
        pass

    def get_term_by_id(self, id):
        """
        query for an ontological term by id
        :param id: str
        :return: term
        """
        pass
