PGDMP     
    .            
    t            notes    9.6.1    9.6.1     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                       false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                       false            �           1262    16384    notes    DATABASE     w   CREATE DATABASE notes WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'en_US.UTF-8' LC_CTYPE = 'en_US.UTF-8';
    DROP DATABASE notes;
             postgres    false                        2615    2200    public    SCHEMA        CREATE SCHEMA public;
    DROP SCHEMA public;
             postgres    false            �           0    0    SCHEMA public    COMMENT     6   COMMENT ON SCHEMA public IS 'standard public schema';
                  postgres    false    3                        3079    12427    plpgsql 	   EXTENSION     ?   CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;
    DROP EXTENSION plpgsql;
                  false            �           0    0    EXTENSION plpgsql    COMMENT     @   COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';
                       false    1            �            1259    16399    notes    TABLE     [   CREATE TABLE notes (
    id bigint NOT NULL,
    note text,
    title character varying
);
    DROP TABLE public.notes;
       public         postgres    false    3            �           0    0    notes    ACL     #   GRANT ALL ON TABLE notes TO notes;
            public       postgres    false    186            �            1259    16397    notes_id_seq    SEQUENCE     n   CREATE SEQUENCE notes_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 #   DROP SEQUENCE public.notes_id_seq;
       public       postgres    false    3    186            �           0    0    notes_id_seq    SEQUENCE OWNED BY     /   ALTER SEQUENCE notes_id_seq OWNED BY notes.id;
            public       postgres    false    185            �            1259    16411    notes_table    TABLE     G   CREATE TABLE notes_table (
    id bigint NOT NULL,
    content json
);
    DROP TABLE public.notes_table;
       public         postgres    false    3            �            1259    16409    test_id_seq    SEQUENCE     m   CREATE SEQUENCE test_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 "   DROP SEQUENCE public.test_id_seq;
       public       postgres    false    188    3            �           0    0    test_id_seq    SEQUENCE OWNED BY     4   ALTER SEQUENCE test_id_seq OWNED BY notes_table.id;
            public       postgres    false    187            �           2604    16402    notes id    DEFAULT     V   ALTER TABLE ONLY notes ALTER COLUMN id SET DEFAULT nextval('notes_id_seq'::regclass);
 7   ALTER TABLE public.notes ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    185    186    186                        2604    16414    notes_table id    DEFAULT     [   ALTER TABLE ONLY notes_table ALTER COLUMN id SET DEFAULT nextval('test_id_seq'::regclass);
 =   ALTER TABLE public.notes_table ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    187    188    188            {          0    16399    notes 
   TABLE DATA               )   COPY notes (id, note, title) FROM stdin;
    public       postgres    false    186          �           0    0    notes_id_seq    SEQUENCE SET     4   SELECT pg_catalog.setval('notes_id_seq', 31, true);
            public       postgres    false    185            }          0    16411    notes_table 
   TABLE DATA               +   COPY notes_table (id, content) FROM stdin;
    public       postgres    false    188   �       �           0    0    test_id_seq    SEQUENCE SET     3   SELECT pg_catalog.setval('test_id_seq', 55, true);
            public       postgres    false    187                       2606    16407    notes notes_pkey 
   CONSTRAINT     G   ALTER TABLE ONLY notes
    ADD CONSTRAINT notes_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public.notes DROP CONSTRAINT notes_pkey;
       public         postgres    false    186    186                       2606    16419    notes_table test_pkey 
   CONSTRAINT     L   ALTER TABLE ONLY notes_table
    ADD CONSTRAINT test_pkey PRIMARY KEY (id);
 ?   ALTER TABLE ONLY public.notes_table DROP CONSTRAINT test_pkey;
       public         postgres    false    188    188            {   �   x���M
� F��)fh7�j~̪7�	���I��o��V(&P7����#�^:�?4j�rV�
�+�����a�r+��W�������1�g��͈7i��$��;2�_8d��L�����sBB������v,a$���;��;~�2�I��6���֢˹��Dy���      }   �   x�UN;�0��)�2#�,�����m��Jc	��"��	�C��I�kӜ�:�8}�~�±g��!��s,ज़\/�!� �Q�gh���9�Q����(a�w��C�i����;�=R"_�ؘ�/�,C��l3l�Bs�8������������Ց�E)�1�J�     