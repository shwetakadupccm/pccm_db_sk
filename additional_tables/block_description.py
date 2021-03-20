import pandas as pd
import string
import helper_function.ask_y_n_statement as ask
import helper_function.pccm_names as names
import sql.add_update_sql as sql


class BlockDescription():

    def __init__(self, fk, file_number, block_id, block_no, user_name):
        self.pk = fk
        self.file_number = file_number
        self.block_id= block_id
        self.block_no = block_no
        self.block_desc_df_cols = names.names_surgery('block_data')
        self.block_type_list = names.names_surgery('block_type_list')
        self.user_name = user_name

    def block_description(self):
        block_desc_df = pd.DataFrame(columns=self.block_desc_df_cols)
        try:
            blocks = int(self.block_no)
            print('number of blocks: ' + str(blocks))
        except ValueError:
            blocks = int(input('Number of blocks in report: '))
        if blocks == 0:
            block_desc_df.loc[blocks] = ['No blocks in report', 'NA', 'NA']
        else:
            block_id_list = self.create_block_id(blocks)
            block_desc_df = self.block_description_df(block_id_list, block_desc_df)
            sql.print_df(block_desc_df)
            check = ask.ask_y_n("Are block descriptions correct?")
            while not check:
                to_correct = ask.ask_y_n("Correct all entries?")
                if not to_correct:
                    to_do =True
                    while to_do:
                        pk_val = 'block_reference'
                        pk = input("Enter block to change: ")
                        #index = block_id_list.index(pk)
                        #print (block_desc_df.loc[index, :])
                        # print(block_desc_df.loc[block_desc_df[pk_val] == 'foo'])
                        data = block_desc_df.loc[block_desc_df[pk_val]==pk]
                        print(data.to_string())
                        # print(block_desc_df.loc[pk])
                        # df_cols = self.block_desc_df_cols[-2]
                        col_change = ask.ask_list("Name of column to change", self.block_desc_df_cols)
                        new_val = input("Enter correct value for " + col_change + ' for ' + pk)
                        block_desc_df.loc[pk, col_change] = new_val
                        sql.print_df(block_desc_df)
                        to_do = ask.ask_y_n("Make more changes?")
                    check = True
                else:
                    block_desc_df = self.block_description_df(block_id_list, block_desc_df)
                    check = ask.ask_y_n("Are block descriptions correct?")
        block_descriptions_all =self.block_description_for_db(block_desc_df)
        return block_desc_df, block_descriptions_all

    @staticmethod
    def block_description_for_db(block_desc_df):
        block_type_list = names.names_surgery('block_type_list')
        block_data_all = []
        for type in block_type_list:
            query_type = 'block_type == ' + '"' + type + '"'
            id_desc = block_desc_df.query(query_type)
            if list(id_desc.shape)[0] == 0:
                block_data_type = ['Not Removed']
                block_data_all.append(block_data_type)
            else:
                block_data_type = []
                pk = list(id_desc['block_reference'])
                desc = list(id_desc['block_description'])
                for index in range(list(id_desc.shape)[0]):
                    data = pk[index] + ": " + desc[index]
                    block_data_type.append(data)
                block_data_type = ["; ".join(block_data_type)]
                block_data_all.append(block_data_type)
        return block_data_all

    def block_description_df(self, block_id_list, block_desc_df):
        for block in block_id_list:
            print("For Block ID " + self.block_id + ', Block reference: ' + block)
            block_type = ask.ask_list("Block type", self.block_type_list)
            block_desc = input("Block Description for block " + block + ": ")
            block_desc_df.loc[block] = [self.pk, self.file_number, self.block_id, block, block_type, block_desc,
                                        self.user_name, sql.last_update()]
        return block_desc_df


    @staticmethod
    def create_block_id(blocks_total):
        block_id_list = []
        frozen = ask.ask_y_n('Are frozen sections (labelled FS) present?')
        no_frozen = 0
        if frozen:
            no_frozen = int(input('Number of frozen sections: '))
            frozen_list = [str(x) for x in range(no_frozen + 1)]
            frozen_id = ['FS-' + s for s in frozen_list[1:]]
        else:
            frozen_id = []
        blocks = blocks_total - no_frozen
        block_id_chunks = list(divmod(blocks, 26))
        chunk = block_id_chunks[0]
        suffix = [i for i in range(chunk)]
        if chunk == 0:
            for j in range(block_id_chunks[1]):
                alph_list = string.ascii_uppercase[j]
                block_id_list.append(alph_list)
        else:
            for i in range(chunk):
                if i == chunk - 1:
                    for j in range(block_id_chunks[1]):
                        alph_list = string.ascii_uppercase[j] + str(i)
                        block_id_list.append(alph_list)
                else:
                    for j in range(26):
                        alph_list = string.ascii_uppercase[j] + suffix[i]
                        block_id_list.append(alph_list)
        block_id_list = block_id_list + frozen_id
        print(", ".join(block_id_list))
        check_list = ask.ask_y_n("Is block list correct?")
        while not check_list:
            block_id_list = []
            check = ask.ask_y_n('Is Frozen series correct?')
            if not check:
                for i in range(blocks_total):
                    block_id = input('Block id of block number ' + str(i + 1) + ': ')
                    block_id_list.append(block_id)
            else:
                block_id_list = frozen_id
                for i in range(blocks):
                    block_id = input('Block id of block number ' + str(i + 1) + ': ')
                    block_id_list.append(block_id)
            print((", ").join(block_id_list))
            check_list = ask.ask_y_n("Is block list correct?")
        return block_id_list


    @staticmethod
    def ihc_report(ihc_type):
        options = ['positive', 'negative', 'equivocal', 'not_done']
        proteins = ['er', 'pr', 'her2', 'fish']
        ihc_status = []
        for protein in proteins:
            option_list = [ihc_type + "_" + protein + '_' + status for status in options]
            category = protein.upper() + ' status'
            ihc_value = ask.ask_list(category, option_list)
            ihc_status.append(ihc_value)
            if protein in {'er', 'pr'}:
                if 'positive' in ihc_value:
                    percent = input(protein.upper() + "(Percent/Grade, Enter '" + protein + "_percent_not_done' if "
                                                                                            "%age not available): ")
                else:
                    percent = ihc_value
                ihc_status.append(percent)
            elif protein == 'her2':
                percent = input("HER2 Grade: ")
                ihc_status.append(percent)
        tumour_ki67 = input("Ki67 Percent, number only, Enter 'Ki67_not_done' if test not done: ")
        data = ihc_status + [tumour_ki67]
        return data

    @staticmethod
    def stage(pathological_pt, pathological_pn, metastasis, prefix):
        if metastasis:
            metastasis_value = 'M1'
        else:
            metastasis_value = 'M0'
        path_stage = prefix + pathological_pt + pathological_pn + metastasis_value
        clinical_stage = 'NA'
        print("Pathological Stage: " + path_stage)
        check = ask.ask_y_n("Is pathological stage correct")
        if not check:
            path_stage = input("Please enter correct pathological stage: ")
        if metastasis:
            clinical_stage = "IV"
        else:
            if prefix == 'yp':
                if pathological_pt == 'T0' and pathological_pn == 'N0':
                    clinical_stage = 'pcr'
                else:
                    clinical_stage = 'nact_treated'
            else:
                if pathological_pn == "N3":
                    clinical_stage = "IIIC"
                elif pathological_pn == "N2":
                    if pathological_pt == "T4":
                        clinical_stage = "IIIB"
                    else:
                        clinical_stage = "IIIA"
                elif pathological_pn == "N1mi":
                    clinical_stage = "IB"
                elif pathological_pn == "N1":
                    if pathological_pt == "T0" or pathological_pt == "T1":
                        clinical_stage = "IIA"
                    elif pathological_pt == "T2":
                        clinical_stage = "IIB"
                    elif pathological_pt == "T3":
                        clinical_stage = "IIIA"
                    elif pathological_pt == "T4":
                        clinical_stage = "IIIB"
                    else:
                        clinical_stage = input("Clinical Staging: ")
                elif pathological_pn == "N0":
                    if pathological_pt == "Tis":
                        clinical_stage = "0"
                    elif pathological_pt == "T1":
                        clinical_stage = "IA"
                    elif pathological_pt == "T2":
                        clinical_stage = "IIA"
                    elif pathological_pt == "T3":
                        clinical_stage = "IIB"
                    elif pathological_pt == "T4":
                        clinical_stage = "IIIB"
                    else:
                        clinical_stage = input("Clinical Staging: ")
        print("Clinical stage: " + clinical_stage)
        print("Based on TNM status", path_stage, "and TABLE 2 of Giuliano et al., 2017, CA CANCER J CLIN 2017;67:290–"
                                                 "303")
        check = ask.ask_y_n("Is clinical stage correct")
        if not check:
            clinical_stage = input("Please enter correct clinical stage: ")
        return path_stage, clinical_stage


def block_location_format():
    block_location = 'To be entered'
    location = False
    while location == False:
        print("Block Location")
        block_cab = input("Cabinet No: ")
        block_drawer = input("Drawer Number: ")
        block_col = input("Column Number: ")
        block_pos = ask.ask_list("Is Block in", ["Front", "Back"])
        block_location = block_cab + "-" + block_drawer + "-" + block_col + block_pos[0]
        print("Block location is " + block_location)
        location = ask.ask_y_n("Is this correct?")
    return block_location


def breast_cancer_subtype(ihc_type = 'biopsy',er='positive', pr='negative', her2='equivocal', her2_grade= '+2',
                          fish='positive'):
    if 'negative' in er and 'negative' in pr and (('negative' in her2 or 'equivocal' in her2) or her2_grade in
                                                  {'0', '+1', '+2'}) and ('negative' in fish or 'not_done' in fish):
        subtype = ihc_type + '_TNBC'
    elif ('positive' in her2 or '+3' in her2_grade) or 'positive' in fish:
        subtype = ihc_type + '_HER2+'
        if 'positive' in er and 'positive' in pr:
            subtype = subtype + 'ER/PR+'
        elif 'positive' in er or 'positive' in pr:
            subtype = subtype + "_" + er + '_' + pr
    elif 'positive' in er and 'positive' in pr:
        subtype = ihc_type + '_ER/PR'
    elif 'not_done' in er or 'not_done' in pr or 'not_done' in her2:
        subtype = ihc_type + '_ihc_not_done'
    else:
        subtype = "; ".join([er, pr, her2, her2_grade, fish])
    return subtype


def check_path_report_entry(conn, cursor, file_number, table_to_check, pk, block_id, number_of_blocks, user_name):
    from reports.biopsy_report import BiopsyData
    from reports.surgery_block import SurgeryBlockData
    table_data = BiopsyData(conn, cursor, file_number, pk, block_id, number_of_blocks, user_name)
    col_name = 'pk'
    if 'surgery' in table_to_check:
        table_data = SurgeryBlockData(conn, cursor, file_number, pk, block_id, number_of_blocks, user_name)
        col_filter = 'fk'
    pk_fk_present = sql.check_pk_fk_exist(cursor, col_name, pk, table_to_check)
    if not pk_fk_present:
        sql.add_pk_fk_to_table(conn, cursor, table_to_check, col_name, pk)
        print("This block_id -'" + block_id + "' for " + file_number + " does not exist in table " +
            table_to_check + ". Enter new record")
        table_data.add_data()
    else:
        todo = ask.ask_option(file_number + " already exists in table " + table_to_check + ".",
                              ["Edit record", "Edit None"])
        if todo == "Edit record":
            table_data.edit_data()
    return