import pandas

class Filter_Gene:

    def filter(self, gene_map_path):
        user_phenotypes = ['myasthenic', 'congenital']
        data_frame = pandas.read_csv(gene_map_path, skipinitialspace=True)
        filtered_data_frame = pandas.DataFrame()
        for user_phenotype in user_phenotypes:
            filtered_data_frame = pandas.concat(
                [filtered_data_frame,
                 data_frame[data_frame['Phenotypes'].str.lower().str.contains(user_phenotype, na=False)]
                 ])
        return filtered_data_frame

filter_gene = Filter_Gene()
filtered_gene = filter_gene.filter('C:/Users/Wellington/Drive/PhD/Workflows/Diagnosis/input/Omim/genemap2.csv')
writer = pandas.ExcelWriter('filtered_genemap.xlsx', engine='xlsxwriter')
filtered_gene.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()