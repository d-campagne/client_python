import unittest
from prometheus_client.exposition import write_to_textfile as w
from prometheus_client.exposition import _bake_output as b
from prometheus_client.coverage import branch_coverage_2
from prometheus_client import CollectorRegistry, generate_latest, CONTENT_TYPE_LATEST
from unittest.mock import patch, mock_open

class TestBakeOutput(unittest.TestCase):
    def test_with_name_in_params(self):
        registry = CollectorRegistry() 
        status, headers, output = b(registry, 'text/plain', 'identity', {'name[]': ['metric_name']}, True)
        self.assertEqual (status, '200 OK')
        self.assertEqual(headers, [('Content-Type', CONTENT_TYPE_LATEST)])
        self.assertEqual(output, generate_latest(registry))

    def test_without_name_params(self):
        registry = CollectorRegistry() 
        status, headers, output = b(registry, 'text/plain', 'identity', {}, True)
        self.assertEqual(status, '200 OK')
        self.assertEqual(headers, [('Content-Type', CONTENT_TYPE_LATEST)])
        self.assertEqual(output, generate_latest(registry))

    def test_with_gzip_compression_enabled_and_accepted(self):
        registry = CollectorRegistry() 
        status, headers, output = b(registry, 'text/plain', 'gzip', {}, False)
        self.assertEqual(status, '200 OK')
        self.assertEqual(headers, [('Content-Type', CONTENT_TYPE_LATEST), ('Content-Encoding', 'gzip')])
        self.assertTrue(output.startswith(b'\x1f\x8b'))

    def test_with_gzip_compression_disabled(self):
        registry = CollectorRegistry() 
        status, headers, output = b(registry, 'text/plain', 'gzip', {}, True)
        self.assertEqual(status, '200 OK')
        self.assertEqual(headers, [('Content-Type', CONTENT_TYPE_LATEST)])
        self.assertFalse(output.startswith(b'\x1f\x8b'))

class TestWriteToTextfile(unittest.TestCase):
    def setUp(self):
        self.path = '/tmp/metrics.prom' 
        self.registry = CollectorRegistry()  

    @patch('prometheus_client.exposition.generate_latest', return_value=b'fake_metrics')  
    @patch('prometheus_client.exposition.open', new_callable=mock_open)  
    @patch('prometheus_client.exposition.os.replace')  
    @patch('prometheus_client.exposition.os.name', 'nt')  
    def test_write_to_textfile_windows(self, mock_generate_latest, mock_open, mock_replace):
        w(self.path, self.registry)
        self.assertIn("write_to_textfile_1", branch_coverage_2)  

    @patch('prometheus_client.exposition.os.name', 'posix')  
    @patch('prometheus_client.exposition.os.rename') 
    @patch('prometheus_client.exposition.open', new_callable=mock_open)  
    @patch('prometheus_client.exposition.generate_latest', return_value=b'fake_metrics')
    def test_write_to_textfile_non_windows(self, mock_generate_latest, mock_open, mock_rename):
        w(self.path, self.registry)
        self.assertIn("write_to_textfile_2", branch_coverage_2)  

if __name__ == '__main__':
    unittest.main()